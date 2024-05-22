import pytest
import requests

from config import config
from src.baseclasses.response import Response
from src.enums.global_enums import GlobalErrors
from src.schemas.post import PostUpdateResponse, PostBase


@pytest.mark.api
@pytest.mark.parametrize(
    "get_post_by_scenario",
    [
        ("post", 201),
        ("post_negative_id", 201),

        ("post_negative_user_id", 422),
        ("post_string_user_id", 422),
        ("post_zero_user_id", 422),

        ("post_without_title", 200),
        ("post_without_body", 200),
        ("post_without_id", 200),
        ("post_without_user_id", 422),
        ("post_empty", 422),
    ],
    indirect=True,
    ids=str
)
def test_update_post(get_post_by_scenario):
    """
    Тестирование ответа от сервера на запрос
    полного (PUT) обновления поста.
    Осуществляются проверки кода статуса,
    header, json-схемы и значения json-полей.

    Метод PUT обновляет объект полностью,
    перезатирая все поля.

    id поста должен быть указан обязательно и валидируется
    с помощью pydantic-схемы PostBase. id поста нельзя
    разрешать изменять. В теле запроса поле id поста должно
    игнорироваться и оставаться неизменным.

    Код статуса при успешном выполнении запроса
    должен быть 201 (объект создан).

    Проверяется тип контента (json) и кодировка (utf-8).

    Pydantic-схема PostUpdateResponse обязывает сервер
    вернуть json-схему со всеми обязательными и заполненными
    полями (title и body необязательны к заполнению).
    """
    post, status_code = get_post_by_scenario
    post_id = 1
    response = requests.put(url=config.SERVICE_URL + f"/posts/{post_id}",
                            json=post)

    response = Response(response)
    response_post_id = response.response_json.get("id")

    PostBase(id=response_post_id)

    response \
        .assert_status_code(status_code) \
        .assert_header("Content-Type",
                       "application/json; charset=utf-8") \
        .validate(PostUpdateResponse)

    assert response_post_id == post_id, GlobalErrors.WRONG_VALUES_NOT_MATCH
