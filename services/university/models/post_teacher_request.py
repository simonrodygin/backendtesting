from pydantic import BaseModel, ConfigDict
from services.university.models.subject import Subject

class PostTeacherRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    first_name: str
    last_name: str
    subject: Subject