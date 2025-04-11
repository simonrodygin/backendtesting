from pydantic import field_validator
from test_frame.services.general.models.base_project import BaseProject
from test_frame.assets.constants import Constants

class BaseGrade(BaseProject):   
    teacher_id: int
    student_id: int
    grade: int
    
    @field_validator("grade")
    def validate_grade(cls, value):
        min = Constants.MIN_GRADE
        max = Constants.MAX_GRADE
        if value < min or value > max:
            raise ValueError(f"Grade must be between {min} and {max}")
        return value