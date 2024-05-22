import pytest
from src.data.posts_data import fake_posts


@pytest.fixture(scope="function")
def get_post_by_scenario(request):
    return fake_posts[request.param[0]], request.param[1]
