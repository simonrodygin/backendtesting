from pydantic import BaseModel, ConfigDict
from typing import Literal

class Degree(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    degree: Literal['Bachelor', 'Master', 'PhD']