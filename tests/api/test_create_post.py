import pytest
import requests

from config import config
from src.schemas.post import PostResponse
from src.baseclasses.response import Response


@pytest.mark.api
@pytest.mark.parametrize(
    "get_post_by_scenario",
    [
        ("post", 201),

        ("post_negative_id", 201),

        ("post_negative_user_id", 422),
        ("post_string_user_id", 422),
        ("post_zero_user_id", 422),

        ("post_without_title", 422),
        ("post_without_body", 422),
        ("post_empty", 422),
    ],
    indirect=True,
    ids=str
)
def test_create_post(get_post_by_scenario):
    """
    Тестирование ответа от сервера на запрос
    создания поста. Осуществляются проверки
    кода статуса, header, json-схемы и значения
    json-полей.

    Код статуса при успешном выполнении запроса
    должен быть 201 (создан объект). При несоответсвии ответа
    сервера pydantic-схеме возвращается ошибка валидации
    (код статуса 422).

    Проверяется тип контента (json) и кодировка (utf-8).

    Pydantic-схема PostResponse обязывает сервер
    вернуть json-схему со всеми существующими полями
    (все поля обязательные к заполнению).
    """
    post, status_code = get_post_by_scenario

    response = requests.post(url=config.SERVICE_URL + "/posts",
                             json=post)
    response = Response(response)

    response \
        .assert_status_code(status_code) \
        .assert_header("Content-Type",
                       "application/json; charset=utf-8") \
        .validate(PostResponse)

    if status_code == 201:
        post["id"] = response.response_json["id"]
        assert response.response_json == post
