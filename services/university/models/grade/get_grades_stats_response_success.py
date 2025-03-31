from services.general.models.standart import Standart


class GetGradesStatsResponseSuccess(Standart):
    count: int
    min: int | None
    max: int | None
    avg: float | None