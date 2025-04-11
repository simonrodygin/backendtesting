from pydantic import BaseModel, ConfigDict

class PostLoginSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    access_token: str
    token_type: str