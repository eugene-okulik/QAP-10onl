import json
import requests


def test_add_meme(domain, authorization):
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorization}'
    }
    my_data = json.dumps(
        {
            "text": "Seafood diet",
            "url": "https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg",
            "tags": ["seafood", "diet"],
            "info": {"type": "jpg"}

        }
    )
    response = requests.post(f'{domain}/meme', headers=my_headers, data=my_data).json()
    assert response['text'] == "Seafood diet"


def test_update_meme(domain, authorization, add_meme):
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorization}'
    }
    my_data = json.dumps(
        {
            "id": add_meme,
            "text": "Seafood diet meme",
            "url": "https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg",
            "tags": ["seafood", "diet"],
            "info": {"type": "jpg"}
        }
    )
    response = requests.put(f'{domain}/meme/{add_meme}', headers=my_headers, data=my_data).json()
    assert response['text'] == 'Seafood diet meme'


def test_delete_meme(domain, authorization, add_meme):
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorization}'
    }
    meme_id = add_meme
    requests.delete(f'{domain}/meme/{meme_id}', headers=my_headers)
    response = requests.get(f'{domain}/meme/{meme_id}', headers=my_headers)
    assert response.status_code == 404


def test_get_meme(domain, authorization):
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorization}'
    }
    response = requests.get(f'{domain}/meme', headers=my_headers).json()['data']
    test_result = False
    for mem in response:
        for tag in mem["tags"]:
            if 'fun' in tag:
                test_result = True
                break
    assert test_result
