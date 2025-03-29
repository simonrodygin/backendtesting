from services.university.models.subject import Subject
from services.general.models.standart import Standart

class Teacher(Standart):  
    first_name: str
    last_name: str
    subject: Subject