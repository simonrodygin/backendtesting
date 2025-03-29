from services.general.models.standart import Standart

class Fail(Standart):
    detail: str | list[dict]