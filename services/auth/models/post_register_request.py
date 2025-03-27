from pydantic import BaseModel, ConfigDict

class PostRegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    username: str
    password: str
    repeat_password: str
    email: str