from requests import Session
import requests
from logger.logger import Logger
import curlify
from utils.json_utils import JsonUtils
import json

def log_response(func):
    def wrapper(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)
        Logger.info(f"Request: {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=2) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status code: {response.status_code}, time: {response.elapsed.total_seconds()}s")
        Logger.info(f"Response: {body}")
        return response
    return wrapper

class SessionUtils:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}
        self.url = url
        self.session = Session()
        self.session.headers.update(headers)

    @log_response
    def get(self, endpoint, **kwargs):
        response = self.session.get(self.url + endpoint, **kwargs)
        return response
    
    @log_response
    def post(self, endpoint, data = None, json = None, **kwargs):
        response = self.session.post(self.url + endpoint, data, json, **kwargs)
        return response
    
    @log_response
    def delete(self, endpoint, **kwargs):
        response = self.session.delete(self.url + endpoint, **kwargs)
        return response
