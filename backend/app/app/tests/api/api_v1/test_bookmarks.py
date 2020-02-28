import requests

from app.core import config
from app.tests.utils.bookmark import create_random_bookmark
from app.tests.utils.utils import get_server_api
from app.tests.utils.user import create_random_user


def test_create_bookmark(superuser_token_headers):
    server_api = get_server_api()
    data = {"title": "Foo", "description": "Fighters"}
    response = requests.post(
        f"{server_api}{config.API_V1_STR}/bookmarks/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_bookmark(superuser_token_headers):
    bookmark = create_random_bookmark()
    server_api = get_server_api()
    response = requests.get(
        f"{server_api}{config.API_V1_STR}/bookmarks/{bookmark.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == bookmark.title
    assert content["description"] == bookmark.description
    assert content["id"] == bookmark.id
    assert content["owner_id"] == bookmark.owner_id
