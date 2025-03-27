from utils.session_utils import SessionUtils
from services.auth.models.post_register_request import PostRegisterRequest
from services.auth.models.post_register_success_response import PostRegisterSuccessResponse
from services.auth.models.post_login_request import PostLoginRequest
from services.auth.models.post_login_success_response import PostLoginSuccessResponse


class AuthenticationHelper:
    ENDPOINT = "/auth"
    REGISTER_ENDPOINT = f"{ENDPOINT}/register/"
    LOGIN_ENDPOINT = f"{ENDPOINT}/login/"

    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils

    def post_register(self, data: PostRegisterRequest) -> PostRegisterSuccessResponse:
        response = self.session_utils.post(self.REGISTER_ENDPOINT, json=data)
        return response
    
    def post_login(self, data: PostLoginRequest) -> PostLoginSuccessResponse:
        response = self.session_utils.post(self.LOGIN_ENDPOINT, json=data)
        return response