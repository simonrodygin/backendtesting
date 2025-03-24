import json

class JsonUtils:
    @staticmethod
    def is_json(json_string: str) -> bool:
        try:
            json.loads(json_string)
        except ValueError:
            return False
        return True