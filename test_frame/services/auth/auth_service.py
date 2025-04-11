from test_frame.utils.session_utils import SessionUtils
from test_frame.services.auth.helpers.authentication_helper import AuthenticationHelper
from test_frame.services.auth.models.post_register_request import PostRegisterRequest
from test_frame.services.auth.models.post_register_success_response import PostRegisterSuccessResponse
from test_frame.services.auth.models.post_login_request import PostLoginRequest
from test_frame.services.auth.models.post_login_success_response import PostLoginSuccessResponse

class AuthService():
    SERVICE_URL = 'http://127.0.0.1:8000/'
    
    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils
        self.auth_helper = AuthenticationHelper(self.session_utils)

    def register(self, data: PostRegisterRequest) -> PostRegisterSuccessResponse:
        response = self.auth_helper.post_register(data.model_dump())
        return PostRegisterSuccessResponse(**response.json())
    
    def login(self, data: PostLoginRequest) -> PostLoginSuccessResponse:
        response = self.auth_helper.post_login(data.model_dump())
        return PostLoginSuccessResponse(**response.json())