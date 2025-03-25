from pydantic import BaseModel, ConfigDict

class PostGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    name: str