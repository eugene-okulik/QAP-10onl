import requests
import json


def test_get_all_meme(base_url, authorisation):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}'
    }
    response = requests.request(
        'GET',
        f'{base_url}/meme',
        headers=header
    ).json()
    fun_tag_counter = 0
    for meme in response['data']:
        if 'fun' in meme['tags']:
            fun_tag_counter += 1
    assert fun_tag_counter > 0, 'memes with "fun" tag must be > 0'


def test_create_new_meme(base_url, authorisation):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}',
    }
    data = json.dumps(
        {
            "text": "Hello memes",
            "url": "https://cdn.kanobu.ru/articles/pics/88f1a95f-63ee-482f-9d04-3ffaf1a44191.webp",
            "tags": [
                "18+"
            ],
            "info": {
                "type": "jpg"
            }
        }
    )
    new_meme = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=header,
        data=data
    ).json()
    assert new_meme['text'] == 'Hello memes'
    assert new_meme['updated_by'] == "evgeny"


def test_delete_meme(base_url, authorisation, prepare_meme):
    meme_id = prepare_meme
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}'
    }
    requests.request(
        'DELETE',
        f'{base_url}/meme/{meme_id}',
        headers=header
    )
    response = requests.request(
        'GET',
        f'{base_url}/meme/{meme_id}',
        headers=header
    )
    assert response.status_code == 404


def test_update_meme(base_url, authorisation, prepare_meme):
    meme_id = prepare_meme
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}'
    }
    data = json.dumps(
        {
            "id": meme_id,
            "text": "Hello memes",
            "url": "https://cdn.kanobu.ru/articles/pics/88f1a95f-63ee-482f-9d04-3ffaf1a44191.webp",
            "tags": [
                "20+"
            ],
            "info": {
                "type": "jpg"
            }
        }
    )
    response = requests.request(
        'PUT',
        f'{base_url}/meme/{meme_id}',
        headers=header,
        data=data
    ).json()
    assert response['tags'] == ['20+']
