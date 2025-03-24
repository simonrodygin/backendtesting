import pytest
from services.auth.auth_service import AuthService
from utils.session_utils import SessionUtils
from faker import Faker
from services.auth.models.register_request import RegisterRequest
from services.auth.models.login_request import LoginRequest

faker = Faker()

@pytest.fixture(scope='function', autouse=False)
def auth_session_utils_anon():
    session_utils = SessionUtils(AuthService.SERVICE_URL)
    return session_utils

@pytest.fixture(scope='function', autouse=False)
def random_user_access_token(auth_session_utils_anon):
    auth_service = AuthService(auth_session_utils_anon)
    username = faker.user_name()
    password = faker.password(length=30, special_chars=True, digits=True, upper_case=True, lower_case=True)
    repeat_password = password
    email = faker.email()

    auth_service.register(data=RegisterRequest(username=username, password=password, repeat_password=repeat_password, email=email))
    response = auth_service.login(data=LoginRequest(username=username, password=password))
    return response.access_token