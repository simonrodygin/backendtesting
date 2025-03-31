from services.university.models.grade.base_grade import BaseGrade
from pydantic import RootModel

from typing import List

class GradeRecord(BaseGrade):
    id: int

class GetGradesResponseSuccess(RootModel):
    root: List[GradeRecord]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]