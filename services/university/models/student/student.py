from services.general.models.standart import Standart
from services.university.models.degree import Degree

class Student(Standart):   
    first_name: str
    last_name: str
    email: str
    degree: Degree
    phone: str
    group_id: int