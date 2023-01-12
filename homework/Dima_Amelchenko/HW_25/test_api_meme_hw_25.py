import requests
import json


def test_add_new_meme(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "Family",
            "url": "https://www.thevoicemag.ru/upload/img_cache/f0e/f0e1c3b4b532fbc70a73e022ffcf35f2_fitted_1332x0.jpg",
            "tags": ["fun", "Vin Diesel"],
            "info": {"type": "jpg"}
        }
    )
    response = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()
    assert response['text'] == "Family"
    assert response['updated_by'] == "Dima_Amelchenko"


def test_modification_meme(domain, token, add_meme):
    headers = {
        'Content-Type': 'application/json', 'Authorization': f'{token}'}
    data = json.dumps(
        {
            f"id": {add_meme},
            "text": "Family",
            "url": "https://www.thevoicemag.ru/upload/img_cache/f0e/f0e1c3b4b532fbc70a73e022ffcf35f2_fitted_1332x0.jpg",
            "tags": ["fun", "Vin Diesel", "The Fast and the Furious"],
            "info": {"type": "jpg"}
        }
    )
    response = requests.request('PUT', f'{domain}/meme/{test_add_new_meme}', headers=headers, data=data).json()
    assert response['tags'] == ["fun", "Vin Diesel", "The Fast and the Furious"]
    assert response['id'] == add_meme


def test_delete_meme(domain, token, add_meme):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{token}'
    }
    requests.request('DELETE', f'{domain}/meme/{add_meme}', headers=headers)
    response = requests.request('GET', f'{domain}/meme/{add_meme}', headers=headers)
    assert response.status_code == 404


def test_teg_fun(domain, authorize):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    response = requests.get(f'{domain}/meme', headers=header).json()['data']
    test_result = False
    for mem in response:
        for tag in mem["tags"]:
            if 'fun' in tag:
                test_result = True
                break
    assert test_result
