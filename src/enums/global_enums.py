from enum import Enum


class GlobalErrors(Enum):
    """
    Обычный класс с ошибками которые стоит использовать в Assert и в
    Response класс. Нужно это для того, чтобы:
    1. Унифицировать всё это дело
    2. Облегчить использование и обновление ошибок
    """
    WRONG_STATUS_CODE = "Status code is different than expected"
    WRONG_HEADER_VALUE = "Header value is different than expected"
    WRONG_JSON_SCHEMA = "Could not map received object to pydantic schema"
    WRONG_VALUES_NOT_MATCH = "Values do not match"
