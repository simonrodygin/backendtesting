from pydantic import BaseModel, ConfigDict

class GetGroupFail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    detail: str | list[dict]