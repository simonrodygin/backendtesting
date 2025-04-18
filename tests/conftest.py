import pytest
from services.auth.auth_service import AuthService
from utils.session_utils import SessionUtils
from faker import Faker
from services.auth.models.post_register_request import PostRegisterRequest
from services.auth.models.post_login_request import PostLoginRequest
from services.university.uni_service import UniService
import time
import requests
from utils.confiig_reader import ConfigReader
from logger.logger import Logger

faker = Faker()
config_reader = ConfigReader()

@pytest.fixture(scope='function', autouse=False)
def auth_session_utils_anon():
    session_utils = SessionUtils(AuthService.SERVICE_URL)
    return session_utils

@pytest.fixture(scope='function', autouse=False)
def random_user_access_token(auth_session_utils_anon):
    auth_service = AuthService(auth_session_utils_anon)
    username = faker.user_name()
    password = faker.password(length=30, special_chars=True, digits=True, upper_case=True, lower_case=True)
    password_repeat = password
    email = faker.email()

    auth_service.register(data=PostRegisterRequest(username=username, password=password, password_repeat=password_repeat, email=email))
    response = auth_service.login(data=PostLoginRequest(username=username, password=password))
    return response.access_token

@pytest.fixture(scope='function', autouse=False)
def uni_session_utils(random_user_access_token):
    session_utils = SessionUtils(UniService.SERVICE_URL, headers={
        'Authorization': f'Bearer {random_user_access_token}'
    })
    return session_utils

@pytest.fixture(scope='function', autouse=False)
def uni_session_utils_anon():
    session_utils = SessionUtils(UniService.SERVICE_URL)
    return session_utils

@pytest.fixture(scope='function', autouse=False)
def uni_session_wrong_creds():
    session_utils = SessionUtils(UniService.SERVICE_URL, headers={'Authorization': 'Bearer wrong'})
    return session_utils

@pytest.fixture(scope='function', autouse=False)
def uni_service(uni_session_utils):
    uni_service = UniService(uni_session_utils)
    return uni_service

@pytest.fixture(scope='function', autouse=False)
def uni_service_anon(uni_session_utils_anon):
    uni_service = UniService(uni_session_utils_anon)
    return uni_service

@pytest.fixture(scope='function', autouse=False)
def uni_service_wrong_creds(uni_session_wrong_creds):
    uni_service = UniService(uni_session_wrong_creds)
    return uni_service

@pytest.fixture(scope='function', autouse=False)
def clean_uni(uni_service):
    yield
    uni_service.clean()

@pytest.fixture(scope='function', autouse=False)
def clean_group_uni(uni_service):
    yield
    uni_service.clean_group()

@pytest.fixture(scope='function', autouse=True)
def auth_readiness_check():
    timeout = config_reader.get_constant("standart_timeout")

    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.request('GET', AuthService.SERVICE_URL + '/docs')
            response.raise_for_status()
        except (ConnectionError, requests.exceptions.Timeout) as e:
            Logger.info(f"Connection error: {e}")
            time.sleep(config_reader.get_constant("standart_poll_frequency"))
        else:
            break
    else:
        raise RuntimeError(f'Auth services did not started during {timeout} sec')
    
@pytest.fixture(scope='function', autouse=False)
def uni_readiness_check():
    timeout = config_reader.get_constant("standart_timeout")

    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.request('GET', UniService.SERVICE_URL + '/docs')
            response.raise_for_status()
        except (ConnectionError, requests.exceptions.Timeout) as e:
            Logger.info(f"Connection error: {e}")
            time.sleep(config_reader.get_constant("standart_poll_frequency"))
        else:
            break
    else:
        raise RuntimeError(f'University services did not started during {timeout} sec')