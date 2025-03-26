from utils.session_utils import SessionUtils
from services.university.models import PostTeacherRequest
from services.university.models import PostTeacherResponseSuccess

class TeacherHelper():
    ENDPOINT = "teachers/"
    
    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils

    def get_teacher(self, teacher_id: int):
        response = self.session_utils.get(self.ENDPOINT + f"{teacher_id}/")
        return response
    
    def get_teachers_list(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_teacher(self, data: PostTeacherRequest) -> PostTeacherResponseSuccess:
        response = self.session_utils.post(self.ENDPOINT, json=data)
        return response
    
    def delete_teacher(self, teacher_id: int):
        response = self.session_utils.delete(self.ENDPOINT + f"{teacher_id}/")
        return response