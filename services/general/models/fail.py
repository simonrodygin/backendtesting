from services.general.models.base_project import BaseProject

class Fail(BaseProject):
    detail: str | list[dict]