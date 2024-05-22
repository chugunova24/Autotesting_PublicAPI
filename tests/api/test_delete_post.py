import pytest
import requests

from config import config
from src.baseclasses.response import Response
from src.schemas.post import PostBase


@pytest.mark.api
@pytest.mark.parametrize(
    "post_id, status_code",
    [
        (1, 204),
        ("", 404),
        (-1, 422),
        (0, 422),
        ("string_id", 422),
        (122, 404),  # пост c id=122 не существует
    ],
    ids=str
)
def test_delete_post(post_id, status_code):
    """
    Тестирование ответа от сервера на запрос
    удаления поста. Осуществляются проверки
    кода статуса и значения
    json-полей.

    Код статуса при успешном выполнении запроса
    должен быть 204 (код ответа, если удаление было
    выполнено, но тело ответа отсутствует).
    """
    response = requests.delete(url=config.SERVICE_URL + f"/posts/{post_id}")
    response = Response(response)

    response.assert_status_code(status_code)
    PostBase(id=post_id)  # валидация поля id

    if status_code == 204:
        assert response.response_json == {}
