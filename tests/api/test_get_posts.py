import pytest
import requests

from config import config
from src.baseclasses.response import Response
from src.schemas.post import PostResponse


@pytest.mark.api
def test_get_posts():
    """
    Тестирование ответа от сервера на запрос
    получения постов. Осуществляются проверки
    кода статуса, header, json-схемы и значения
    json-полей, количество постов в ответе.

    Код статуса при успешном выполнении запроса
    должен быть 200.

    Количество постов в ответе должно быть ограничено
    (например, в данном эндпоинте не реализован пагинатор
    или любой другой способ ограничения кол-ва постов).

    Проверяется тип контента (json) и кодировка (utf-8).

    Pydantic-схема PostResponse обязывает сервер
    вернуть json-схему со всеми существующими полями
    (все поля обязательные к заполнению).
    """
    response = requests.get(url=config.SERVICE_URL + "/posts")
    response = Response(response)

    response \
        .assert_status_code(200) \
        .assert_header("Content-Type",
                       "application/json; charset=utf-8") \
        .validate(PostResponse)

    assert len(response.response_json) <= 20, "Check number of posts"
