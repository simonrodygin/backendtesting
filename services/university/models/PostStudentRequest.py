from pydantic import BaseModel, ConfigDict
from services.university.models.degree import Degree

class PostStudentRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    email: str
    degree: Degree
    phone: str
    group_id: int