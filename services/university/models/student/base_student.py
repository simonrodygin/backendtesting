from services.general.models.standart import Standart
from services.university.models.degree_enum import DegreeEnum

class BaseStudent(Standart):   
    first_name: str
    last_name: str
    email: str
    degree: DegreeEnum
    phone: str
    group_id: int