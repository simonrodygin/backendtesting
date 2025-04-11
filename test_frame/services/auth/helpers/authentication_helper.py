from test_frame.services.general.helpers.base_helper import BaseHelper


class AuthenticationHelper(BaseHelper):
    ENDPOINT = "/auth"
    REGISTER_ENDPOINT = f"{ENDPOINT}/register/"
    LOGIN_ENDPOINT = f"{ENDPOINT}/login/"

    def post_register(self, data):
        response = self.session_utils.post(self.REGISTER_ENDPOINT, data=data)
        return response
    
    def post_login(self, data):
        response = self.session_utils.post(self.LOGIN_ENDPOINT, data=data)
        return response