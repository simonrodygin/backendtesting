from test_frame.services.university.models.grade.base_grade import BaseGrade
from test_frame.services.general.models.base_root import BaseRoot

from typing import List

class GradeRecord(BaseGrade):
    id: int

class GetGradesResponseSuccess(BaseRoot):
    root: List[GradeRecord]