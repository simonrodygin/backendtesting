from services.general.helpers.base_helper import BaseHelper
from typing import Literal, Dict, Any
from string import Template

class GradeHelper(BaseHelper):
    ENDPOINT = "grades"
    STATS_ENDPOINT = fr"{ENDPOINT}/stats/"
    ENDPOINT_WITH_ID = Template("{self.ENDPOINT}/$ID/")

    def get_grades(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def get_stats(self, search_by_id = None):
        if search_by_id is None:
            response = self.session_utils.get(self.STATS_ENDPOINT)
        elif isinstance(search_by_id, Dict[Literal['group_id', 'student_id', 'teacher_id'], Any]): 
            search_by_id = {key: value for key, value in search_by_id.items() if value is not None}
            response = self.session_utils.get(self.STATS_ENDPOINT, params=search_by_id)
        else:
            response = self.session_utils.get(self.STATS_ENDPOINT, params=search_by_id)
        return response

    def post_grade(self, data):
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def put_grade(self, data, grade_id: int):
        response = self.session_utils.put(self.ENDPOINT_WITH_ID.substitute(ID=grade_id), data=data)
        return response
    
    def delete_grade(self, grade_id: int):
        response = self.session_utils.delete(self.ENDPOINT_WITH_ID.substitute(ID=grade_id))
        return response