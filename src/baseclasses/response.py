from pydantic.error_wrappers import ValidationError
from src.enums.global_enums import GlobalErrors


class Response:

    """
    Полезный класс, который помогает нам экономить тонны кода в процессе
    валидации данных. На вход он принимает объект респонса и разбирает его.
    Вы можете добавить кучу различных методов в этом классе, которые нужны
    вам в работе с данными после их получения.
    """

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        try:
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    parsed_object = schema.parse_obj(item)
                    self.parsed_object = parsed_object
            else:
                schema.parse_obj(self.response_json)
        except ValidationError:
            raise AssertionError(
                GlobalErrors.WRONG_JSON_SCHEMA
            )

    def assert_status_code(self, status_code):
        """
        Метод для валидации статус кода. Из объекта респонса,
        который мы получили, мы берём статус и сравнимаем с тем, который
        нам был передан как параметр.
        """
        assert self.response_status == status_code, GlobalErrors.WRONG_STATUS_CODE
        return self

    def assert_header(self, header, expectation):
        assert self.response.headers[header] == expectation, GlobalErrors.WRONG_HEADER_VALUE
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        """
        Метод отвечает за строковое представление нашего объекта. Что весьма
        удобно, ведь в случае срабатывания валидации, мы получаем полную картину
        всего происходящего и все параметры которые нам нужны для определения
        ошибки.
        """
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"
