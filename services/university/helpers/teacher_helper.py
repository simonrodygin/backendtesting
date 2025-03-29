from utils.session_utils import SessionUtils
from services.university.models.teacher.post_teacher_request import PostTeacherRequest
from services.university.models.teacher.post_teacher_response_success import PostTeacherResponseSuccess
from services.general.helpers.base_helper import BaseHelper

class TeacherHelper(BaseHelper):
    ENDPOINT = "teachers/"

    def get_teacher(self, teacher_id: int):
        response = self.session_utils.get(self.ENDPOINT + f"{teacher_id}/")
        return response
    
    def get_teachers(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_teacher(self, data: PostTeacherRequest) -> PostTeacherResponseSuccess:
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def delete_teacher(self, teacher_id: int):
        response = self.session_utils.delete(self.ENDPOINT + f"{teacher_id}/")
        return response