from pydantic import BaseModel, ConfigDict

class RegisterSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    detail: str