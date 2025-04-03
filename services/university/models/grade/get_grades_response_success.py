from services.university.models.grade.base_grade import BaseGrade
from services.general.models.base_root import BaseRoot

from typing import List

class GradeRecord(BaseGrade):
    id: int

class GetGradesResponseSuccess(BaseRoot):
    root: List[GradeRecord]