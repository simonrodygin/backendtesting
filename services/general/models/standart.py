from pydantic import BaseModel, ConfigDict

class Standart(BaseModel):
    model_config = ConfigDict(extra="forbid")