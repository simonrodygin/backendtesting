from services.general.helpers.base_helper import BaseHelper

class GroupHelper(BaseHelper):
    ENDPOINT = "groups/"

    def get_group(self, group_id: int):
        response = self.session_utils.get(self.ENDPOINT + f"{group_id}/")
        return response
    
    def get_groups(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_group(self, data):
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def delete_group(self, group_id: int):
        response = self.session_utils.delete(self.ENDPOINT + f"{group_id}/")
        return response