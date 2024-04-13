from pydantic import BaseModel, validator

class SessionData(BaseModel):
    expert_domain: str
    user_name: str
    llm_model: str
    embedding_model: str

    @validator("*")
    def empty_string_validator(cls, v):
        if isinstance(v, str) and v.strip() == "":
            raise ValueError("Field cannot be an empty string")
        return v

class AIResponse(BaseModel):
    message: str
    references: dict

