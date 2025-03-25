from pydantic import BaseModel, ConfigDict, field_validator

class PostGradeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    teacher_id: int
    student_id: int
    grade: int
    
    @field_validator("grade")
    def validate_grade(cls, value):
        if value < 0 or value > 5:
            raise ValueError("Grade must be between 0 and 5")
        return value