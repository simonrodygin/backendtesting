from utils.session_utils import SessionUtils
from services.university.models.student.post_student_request import PostStudentRequest
from services.university.models.student.post_student_response_success import PostStudentResponseSuccess
from services.general.helpers.base_helper import BaseHelper

class StudentHelper(BaseHelper):
    ENDPOINT = "students/"

    def get_student(self, student_id: int):
        response = self.session_utils.get(self.ENDPOINT + f"{student_id}/")
        return response
    
    def get_students(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_student(self, data: PostStudentRequest) -> PostStudentResponseSuccess:
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def delete_student(self, student_id: int):
        response = self.session_utils.delete(self.ENDPOINT + f"{student_id}/")
        return response