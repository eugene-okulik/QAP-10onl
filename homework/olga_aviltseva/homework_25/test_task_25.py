import json
import requests


def test_add_meme(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "Best meme generator",
            "url": "https://www.bouncegeek.com/wp-content/uploads/2017/10/Best-meme-generator-min.jpg",
            "tags": ["look"],
            "info": {"type": "png"}
        }
    )
    response = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()
    assert response['text'] == 'Best meme generator'


def test_update_meme(domain, authorize, add_meme):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "id": add_meme,
            "text": "Memes Everywhere",
            "url": "http://4.bp.blogspot.com/-EBM213mALjM/VSUKoz_t0CI/AAAAAAAAuKs/xf5lgQll82k/s1600/meme%2B(2).jpg",
            "tags": ["everywhere"],
            "info": {"type": "png"}
        }
    )

    response = requests.request("PUT", f'{domain}/meme/{add_meme}', headers=headers, data=data).json()
    assert response['text'] == "Memes Everywhere"


def test_delete_meme(domain, authorize, add_meme):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    meme_id = add_meme
    requests.request('DELETE', f'{domain}/meme/{meme_id}', headers=headers)
    response = requests.request("GET", f'{domain}/meme/{meme_id}', headers=headers)
    assert response.status_code == 404


def test_get_memes(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    response = requests.request("GET", f'{domain}/meme', headers=headers).json()['data']
    test_result = False
    for mem in response:
        for tag in mem["tags"]:
            if 'fun' in tag:
                test_result = True
                break
    assert test_result
