from test_frame.services.university.models.subject_enum import SubjectEnum
from test_frame.services.general.models.base_project import BaseProject

class BaseTeacher(BaseProject):  
    first_name: str
    last_name: str
    subject: SubjectEnum