from services.general.helpers.base_helper import BaseHelper
from typing import Literal, Optional

class GradeHelper(BaseHelper):
    ENDPOINT = "grades/"
    STATS_ENDPOINT = f"{ENDPOINT}stats/"

    def get_grades(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def get_stats(self, search_by: Optional[Literal['group_id', 'student_id', 'teacher_id']], id: Optional[int]):
        response = self.session_utils.get(self.STATS_ENDPOINT + f'?{search_by}={id}')
        return response

    def post_grade(self, data):
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def put_grade(self, data, grade_id: int):
        response = self.session_utils.put(self.ENDPOINT  + f"{grade_id}/", data=data)
        return response
    
    def delete_grade(self, grade_id: int):
        response = self.session_utils.delete(self.ENDPOINT + f"{grade_id}/")
        return response