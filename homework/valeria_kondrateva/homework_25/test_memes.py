import json
import requests


def test_add_meme(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "Dog meme",
            "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.wikipedia."
            "org%2Fwiki%2F%25D0%2594%25D0%25BE%25D0%25B3%25D0%25B5&psig=AOvVaw3IUmNjd0m098Jdl_2RxzfY&ust"
            "=1671723797314000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMDj0_eGi_wCFQAAAAAdAAAAABAD",
            "tags": ["fun", "dog"],
            "info": "picture"
        }
    )
    response = requests.request(
        'POST',
        f'{domain}/meme',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == 'Dog meme'


def test_update_meme(domain, authorize, add_meme):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "Dog meme - UPDATED",
            "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.wikipedia."
            "org%2Fwiki%2F%25D0%2594%25D0%25BE%25D0%25B3%25D0%25B5&psig=AOvVaw3IUmNjd0m098Jdl_2RxzfY&ust"
            "=1671723797314000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMDj0_eGi_wCFQAAAAAdAAAAABAD",
            "tags": ["fun", "dog"],
            "info": "picture"
        }
    )
    response = requests.request(
        'PUT',
        f'{domain}/meme/{add_meme}',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == 'Dog meme - UPDATED'


def test_delete_meme(domain, authorize, add_meme):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    meme_id = add_meme
    requests.request('DELETE', f'{domain}/meme/{meme_id}', headers=headers)
    response = requests.request('GET', f'{domain}/meme/{meme_id}', headers=headers)
    assert response.status_code == 404


def test_get_all_memes(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    response = requests.request('GET', f'{domain}/meme', headers=headers).json()['data']
    test_result = False
    for mem in response:
        for tag in mem["tags"]:
            if 'fun' in tag:
                test_result = True
                break
    assert test_result
