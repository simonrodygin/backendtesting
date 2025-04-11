from test_frame.services.general.models.base_project import BaseProject


class GetGradesStatsResponseSuccess(BaseProject):
    count: int
    min: int | None
    max: int | None
    avg: float | None