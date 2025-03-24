from utils.session_utils import SessionUtils


class UserHelper:
    ENDPOINT = "/users"
    ME_ENDPOINT = f"{ENDPOINT}/me"
    
    def __init__(self, api_utils: SessionUtils):
        self.api_utils = api_utils

    def get_me(self):
        response = self.api_utils.get(self.ME_ENDPOINT)
        return response