import pytest
from services.auth.auth_service import AuthService
from utils.session_utils import SessionUtils
from faker import Faker
from services.auth.models.register_request import RegisterRequest
from services.auth.models.login_request import LoginRequest
from services.university.uni_service import UniService

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

@pytest.fixture(scope='function', autouse=False)
def uni_session_utils_anon(random_user_access_token):
    session_utils = SessionUtils(UniService.SERVICE_URL, headers={
        'Authorization': f'Bearer {random_user_access_token}'
    })
    return session_utils

@pytest.fixture(scope='function', autouse=False)
def uni_service(uni_session_utils_anon):
    uni_service = UniService(uni_session_utils_anon)
    return uni_service