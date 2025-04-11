from services.university.models.subject_enum import SubjectEnum
from services.general.models.base_project import BaseProject

class BaseTeacher(BaseProject):  
    first_name: str
    last_name: str
    subject: SubjectEnum