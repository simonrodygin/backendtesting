from pydantic import BaseModel, ConfigDict

class PostLoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str
    password: str