from utils.session_utils import SessionUtils

class UserHelper:
    ENDPOINT = "users/"
    ME_ENDPOINT = f"{ENDPOINT}me"
    
    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils

    def get_me(self):
        response = self.session_utils.get(self.ME_ENDPOINT)
        return response