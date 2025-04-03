from pydantic import BaseModel, ConfigDict

class BaseProject(BaseModel):
    model_config = ConfigDict(extra="forbid")