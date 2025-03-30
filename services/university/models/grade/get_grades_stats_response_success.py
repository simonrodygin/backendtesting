from services.general.models.standart import Standart

class GetGradesStatsResponseSuccess(Standart):
    count: int
    min: int
    max: int
    avg: float