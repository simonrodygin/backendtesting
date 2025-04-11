from utils.session_utils import SessionUtils

class BaseHelper:
    ENDPOINT: str

    def __init__(self, session_utils: SessionUtils):
        self.session_utils = session_utils