from utils.session_utils import SessionUtils
from services.university.models.post_group_request import PostGroupRequest
from services.university.models.post_group_response_success import PostGroupResponseSuccess

class GroupHelper():
    ENDPOINT = "groups/"
    
    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils

    def get_group(self, group_id: int):
        response = self.session_utils.get(self.ENDPOINT + f"{group_id}/")
        return response
    
    def get_groups_list(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_group(self, data: PostGroupRequest) -> PostGroupResponseSuccess:
        response = self.session_utils.post(self.ENDPOINT, json=data)
        return response
    
    def delete_group(self, group_id: int):
        response = self.session_utils.delete(self.ENDPOINT + f"{group_id}/")
        return response