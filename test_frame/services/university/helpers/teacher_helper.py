from test_frame.services.general.helpers.base_helper import BaseHelper
from string import Template

class TeacherHelper(BaseHelper):
    ENDPOINT = "teachers"
    ENDPOINT_WITH_ID = Template("{self.ENDPOINT}/$ID/")

    def get_teacher(self, teacher_id: int):
        response = self.session_utils.get(self.ENDPOINT_WITH_ID.substitute(ID=teacher_id))
        return response
    
    def get_teachers(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_teacher(self, data):
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def delete_teacher(self, teacher_id: int):
        response = self.session_utils.delete(self.ENDPOINT_WITH_ID.substitute(ID=teacher_id))
        return response