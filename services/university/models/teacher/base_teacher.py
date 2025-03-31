from services.university.models.subject_enum import SubjectEnum
from services.general.models.standart import Standart

class BaseTeacher(Standart):  
    first_name: str
    last_name: str
    subject: SubjectEnum