from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import os
import json
from dotenv import load_dotenv
from deployment import _log
from deployment._chatbot import AIResponse, SessionData
from chatbot.ai_assistant import AI_Assistant

# Load environment variables from .env file
load_dotenv()

# Create a FastAPI instance
app = FastAPI()

# Logger
logger = _log.get_logger(__name__)
logger.info("API is starting up")

# Add SessionMiddleware to the application
app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ["MIDDLEWARE_SECRET_KEY"]
)
ai_assistant = AI_Assistant()
templates = Jinja2Templates(
    directory="templates"
) 

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Log the error details
    logger.error(f"Validation error: {exc.errors()}")
    # You can also include the request body in the log if needed
    body = await request.body()
    logger.error(f"Request body: {body}")
    # Return the standard 422 error response
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

# Get into the main page
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
# Load the options for domains, embedding_providers, llm_models
@app.get("/data/{data_type}")
async def get_data(data_type: str):
    try:
        with open(f"./data/{data_type}.json", "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": "Data not found"}

@app.post("/user/sessionData")
async def submit_form(session_data: SessionData, request: Request):
    global ai_assistant
    # logger.info(f"Received session data: {session_data}")
    request.session["session_data"] = session_data.model_dump()
    ai_assistant.setup(request.session["session_data"])
    # logger.info("/user/sessionData - " + session_data.model_dump())

    # if globals()["chain"] is None:
    #     globals()["chain"] = ai_assistant.create_chain(request.session["session_data"])
    return session_data.model_dump()

# @app.get("/user/sessionData")
# async def get_session_data(request: Request) -> SessionData:
#     session_data = request.session.get("session_data")
#     return SessionData(**session_data)

@app.get("/user/chat")
async def chat(request: Request):
    session_data = request.session.get("session_data")
    return templates.TemplateResponse(
        "chat_ui.html", {"request": request, "session_data": session_data}
    )

@app.post("/user/chat")
async def chat(request: Request, message: str) -> AIResponse:
    logger.info(f"Message: {message}")
    logger.info(f"User Name: {ai_assistant.user_name}")
    ai_response = "Sorry, Im unable to process your message at the moment"
    reference_string = {}
    try:
        ai_response, reference_string = ai_assistant.chat(message)
    except Exception as e:
        logger.error(f"Failed to fetch response from AI:\nError: {e}")

    return AIResponse(message=ai_response, references=reference_string)

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)