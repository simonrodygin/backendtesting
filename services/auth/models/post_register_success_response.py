from pydantic import BaseModel, ConfigDict

class PostRegisterSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    detail: str