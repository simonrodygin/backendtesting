from pydantic import field_validator
from services.general.models.base_project import BaseProject
from utils.confiig_reader import ConfigReader

config_reader = ConfigReader()

class BaseGrade(BaseProject):   
    teacher_id: int
    student_id: int
    grade: int
    
    @field_validator("grade")
    def validate_grade(cls, value):
        min = config_reader.get_constant('min_grade')
        max = config_reader.get_constant('max_grade')
        if value < min or value > max:
            raise ValueError(f"Grade must be between {min} and {max}")
        return value