from pydantic import BaseModel, ConfigDict

class PostRegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    username: str
    password: str
    password_repeat: str
    email: str