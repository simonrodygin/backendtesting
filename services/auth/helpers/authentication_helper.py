from utils.session_utils import SessionUtils


class AuthenticationHelper:
    ENDPOINT = "/auth"
    REGISTER_ENDPOINT = f"{ENDPOINT}/register/"
    LOGIN_ENDPOINT = f"{ENDPOINT}/login/"

    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils

    def post_register(self, data: dict):
        response = self.session_utils.post(self.REGISTER_ENDPOINT, json=data)
        return response
    
    def post_login(self, data: dict):
        response = self.session_utils.post(self.LOGIN_ENDPOINT, json=data)
        return response