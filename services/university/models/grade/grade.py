from pydantic import field_validator
from services.general.models.standart import Standart

class Grade(Standart):   
    teacher_id: int
    student_id: int
    grade: int
    
    @field_validator("grade")
    def validate_grade(cls, value):
        if value < 0 or value > 5:
            raise ValueError("Grade must be between 0 and 5")
        return value