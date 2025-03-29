from pydantic import BaseModel, ConfigDict

class GetGroupSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    name: str