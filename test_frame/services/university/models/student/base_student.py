from test_frame.services.general.models.base_project import BaseProject
from test_frame.services.university.models.degree_enum import DegreeEnum

class BaseStudent(BaseProject):   
    first_name: str
    last_name: str
    email: str
    degree: DegreeEnum
    phone: str
    group_id: int