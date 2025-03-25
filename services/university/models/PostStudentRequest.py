from pydantic import BaseModel, ConfigDict
from typing import Literal

class PostStudentRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    email: str
    degree: Literal['Bachelor', 'Master', 'PhD']
    phone: str
    group_id: int