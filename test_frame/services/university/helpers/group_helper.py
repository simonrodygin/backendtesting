from test_frame.services.general.helpers.base_helper import BaseHelper
from string import Template

class GroupHelper(BaseHelper):
    ENDPOINT = "groups"
    ENDPOINT_WITH_ID = Template(f"{ENDPOINT}/$ID")

    def get_group(self, group_id: int):
        response = self.session_utils.get(self.ENDPOINT_WITH_ID.substitute(ID=group_id))
        return response
    
    def get_groups(self):
        response = self.session_utils.get(self.ENDPOINT)
        return response
    
    def post_group(self, data):
        response = self.session_utils.post(self.ENDPOINT, data=data)
        return response
    
    def delete_group(self, group_id: int):
        response = self.session_utils.delete(self.ENDPOINT_WITH_ID.substitute(ID=group_id))
        return response