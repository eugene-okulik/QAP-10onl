import json
import requests


def test_create_meme(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "mem1",
            "url": "https://cs13.pikabu.ru/post_img/2023/01/11/10/167345632116998858.webp",
            "tags": ["fun", "laptop"],
            "info": {
                "type": "jpg"
            }
        }
    )
    response = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()
    assert response['text'] == "mem1"


def test_update_post(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "id": "247",
            "text": "mem2",
            "url": "https://cs13.pikabu.ru/post_img/2023/01/11/10/167345632116998858.webp",
            "tags": ["fun", "laptop"],
            "info": {
                "type": "jpg"
            }
        }
    )
    response = requests.request('PUT', f'{domain}/meme/247', headers=headers, data=data).json()
    assert response['text'] == 'mem2'


def test_delete_post(domain, authorize, prepare_post):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    requests.request('DELETE', f'{domain}/meme/{prepare_post}', headers=headers)
    response = requests.request('GET', f'{domain}/meme/{prepare_post}', headers=headers)
    print(response)


def test_get_all_memes(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    response = requests.request('GET', f'{domain}/meme', headers=headers).json()
    assert len(response) == 1
    assert response['tags'] == 'fun'
