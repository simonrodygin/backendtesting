from services.general.helpers.base_helper import BaseHelper
from string import Template

class StudentHelper(BaseHelper):
    ENDPOINT = "students"
    ENDPOINT_WITH_ID = Template("{self.ENDPOINT}/$ID/")

    def get_student(self, student_id: int):
        response = self.session_utils.get(self.ENDPOINT_WITH_ID.substitute(ID=student_id))
        return response
    
    def get_students(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_student(self, data):
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def delete_student(self, student_id: int):
        response = self.session_utils.delete(self.ENDPOINT_WITH_ID.substitute(ID=student_id))
        return response