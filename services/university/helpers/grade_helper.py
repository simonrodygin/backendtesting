from utils.session_utils import SessionUtils
from services.university.models.grade.post_grade_request import PostGradeRequest
from services.university.models.grade.post_grade_response_success import PostGradeResponseSuccess
from services.general.helpers.base_helper import BaseHelper

class GradeHelper(BaseHelper):
    ENDPOINT = "grades/"

    def get_grade(self, grade_id: int):
        response = self.session_utils.get(self.ENDPOINT + f"{grade_id}/")
        return response
    
    def get_grades(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_grade(self, data: PostGradeRequest) -> PostGradeResponseSuccess:
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def delete_grade(self, grade_id: int):
        response = self.session_utils.delete(self.ENDPOINT + f"{grade_id}/")
        return response