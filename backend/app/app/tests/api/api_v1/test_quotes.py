import requests

from app.core import config
from app.tests.utils.quote import create_random_quote
from app.tests.utils.tag import create_random_tag
from app.tests.utils.utils import get_server_api
from app.tests.utils.user import create_random_user


def test_create_quote(superuser_token_headers):
    server_api = get_server_api()
    data = {"title": "Foo", "text": "Chicken", "description": "Fighters", "public": "true"}
    response = requests.post(
        f"{server_api}{config.API_V1_STR}/quotes/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_quote(superuser_token_headers):
    quote = create_random_quote()
    server_api = get_server_api()
    response = requests.get(
        f"{server_api}{config.API_V1_STR}/quotes/{quote.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == quote.title
    assert content["description"] == quote.description
    assert content["id"] == quote.id
    assert content["owner_id"] == quote.owner_id

def test_create_quote_with_tag(superuser_token_headers):
    quote = create_random_quote()
    tag = create_random_tag()
    server_api = get_server_api()
    response = requests.get(
        f"{server_api}{config.API_V1_STR}/quotes/{quote.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == quote.title
    assert content["description"] == quote.description
    assert content["id"] == quote.id
    assert content["owner_id"] == quote.owner_id