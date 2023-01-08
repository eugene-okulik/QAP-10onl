import requests
import json


def test_add_meme(domain, auth):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{auth}'
    }
    data = json.dumps(
        {
            "text": "you are very boring, but you can continue",
            "url": "http://risovach.ru/upload/2019/06/mem/kapibara-odobryaet_211465163_orig_.jpg",
            "tags": [
                "capybara",
                "meme",
                "fun"
            ],
            "info": {
                "colors": [
                    "brown",
                    "red",
                    "white"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            }
        }
    )
    response = requests.request(
        'POST',
        f'{domain}/meme',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == 'you are very boring, but you can continue'


def test_update_meme(domain, auth, add_meme):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{auth}'
    }
    data = json.dumps(
        {
            "id": add_meme,
            "text": 'you are very boring, but you can continue updated',
            "url": "http://risovach.ru/upload/2019/06/mem/kapibara-odobryaet_211465163_orig_.jpg",
            "tags": [
                "capybara",
                "meme"
            ],
            "info": {
                "colors": [
                    "brown",
                    "red"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            }
        }
    )
    response = requests.request(
        'PUT',
        f'{domain}/meme/{add_meme}',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == 'you are very boring, but you can continue updated'


def test_delete_meme(domain, auth, add_meme):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{auth}'
    }
    requests.request(
        'DELETE',
        f'{domain}/meme/{add_meme}',
        headers=headers
    )
    response = requests.request(
        'GET',
        f'{domain}/meme/{add_meme}',
        headers=headers
    )
    assert response.status_code == 404


def test_get_all_memes(domain, auth):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{auth}'
    }
    response = requests.request(
        'GET',
        f'{domain}/meme',
        headers=headers
    ).json()
    fun_tags_count = 0
    for meme in response['data']:
        if 'fun' in meme['tags']:
            fun_tags_count += 1
    assert fun_tags_count > 0, "no memes with fun tag"
