import json
import requests


def test_create_new_meme(domain, authorisation):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}',
    }
    data = json.dumps(
        {
            "text": "My new mem",
            "url": "https://klike.net/uploads/posts/2019-09/1568449912_2.jpg",
            "tags": [
                "Cats"
            ],
            "info": {
                "type": "jpg"
            }
        }
    )
    create_meme = requests.request(
        'POST',
        f'{domain}/meme',
        headers=header,
        data=data
    ).json()
    assert create_meme['text'] == 'My new mem'
    assert create_meme['tags'] == ['Cats']


def test_update_meme(domain, authorisation, prepare_post):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}'
    }
    data = json.dumps(
        {
            "id": prepare_post,
            "text": "My new mem",
            "url": "https://klike.net/uploads/posts/2019-09/1568449912_2.jpg",
            "tags": [
                "Kitty"
            ],
            "info": {
                "type": "jpg"
            }
        }
    )
    response = requests.request(
        'PUT',
        f'{domain}/meme/{prepare_post}',
        headers=header,
        data=data
    ).json()
    assert response['tags'] == ['Kitty']


def test_delete_mem(domain, authorisation, prepare_post):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}'
    }
    requests.request(
        'DELETE',
        f'{domain}/meme/{prepare_post}',
        headers=header
    )
    response = requests.request(
        'GET',
        f'{domain}/meme/{prepare_post}',
        headers=header
    )
    assert response.status_code == 404


def test_get_all_meme(domain, authorisation):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}'
    }
    response = requests.request(
        'GET',
        f'{domain}/meme',
        headers=header
    ).json()
    fun_tag = 0
    for meme in response['data']:
        if 'fun' in meme['tags']:
            fun_tag += 1
    assert fun_tag > 0, 'Meme tagged "fun" exist'
