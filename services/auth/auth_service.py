from utils.session_utils import SessionUtils
from services.auth.helpers.authentication_helper import AuthenticationHelper
from services.auth.helpers.user_helper import UserHelper
from services.auth.models.register_request import RegisterRequest
from services.auth.models.register_success_response import RegisterSuccessResponse
from services.auth.models.login_request import LoginRequest
from services.auth.models.login_success_response import LoginSuccessResponse

class AuthService():
    SERVICE_URL = 'http://127.0.0.1:8000'
    
    def __init__(self, api_utils: SessionUtils):
        self.api_utils = api_utils
        self.auth_helper = AuthenticationHelper(api_utils)
        self.user_helper = UserHelper(api_utils)

    def register(self, data: RegisterRequest) -> RegisterSuccessResponse:
        response = self.auth_helper.post_register(data.model_dump())
        return RegisterSuccessResponse(**response.json())
    
    def login(self, data: LoginRequest) -> LoginSuccessResponse:
        response = self.auth_helper.post_login(data.model_dump())
        return LoginSuccessResponse(**response.json())