from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a FastAPI instance
app = FastAPI()

# Add SessionMiddleware to the application
app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ["MIDDLEWARE_SECRET_KEY"]
)

# A simple route that sets a session variable
@app.get("/set-session/{username}")
async def set_session(request: Request, username: str):
    request.session['username'] = username
    return {"message": f"Session for {username} is set."}

# A simple route that retrieves a session variable
@app.get("/get-session")
async def get_session(request: Request):
    username = request.session.get('username')
    if username:
        return {"message": f"Welcome back, {username}!"}
    return {"message": "No active session found."}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)