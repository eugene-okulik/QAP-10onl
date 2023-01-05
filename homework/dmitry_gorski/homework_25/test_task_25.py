import json
import requests


def test_create_meme(domain, authorize):
    headers, endpoint = {"Authorization": f'{authorize}', 'Content-Type': 'application/json'}, '/meme'
    data_json = {
        'text': 'Which fucking monday',
        'url': 'https://cdn.memes.com/up/36793211618339628/i/1671475140893.jpg',
        'tags': ['monday', 'products'],
        'info': {'colors': ['green', 'white', 'red'],
                 'objects': ['products', 'products_info']}
    }
    data = json.dumps(data_json)
    response = requests.post(f'{domain}{endpoint}', headers=headers, data=data).json()
    assert response['url'] == data_json['url']


def test_update_meme(domain, authorize, create_meme):
    headers, endpoint = {"Authorization": f'{authorize}', 'Content-Type': 'application/json'}, '/meme'
    meme_id = create_meme
    data_json = {
        'id': create_meme,
        'text': 'Minecraft reference',
        'url': 'https://cdn.memes.com/up/36793211618339628/i/1671480485483.jpg',
        'tags': ['man', 'hairstyle', 'minecraft'],
        'info': {'colors': ['green', 'brown'],
                 'objects': ['man', 'cube']}
    }
    data = json.dumps(data_json)
    response = requests.put(f'{domain}{endpoint}/{meme_id}', headers=headers, data=data).json()
    assert response['url'] == data_json['url']


def test_delete_meme(domain, authorize, create_meme):
    headers, endpoint = {"Authorization": f'{authorize}', 'Content-Type': 'application/json'}, '/meme'
    meme_id = create_meme
    requests.delete(f'{domain}{endpoint}/{meme_id}', headers=headers)
    response = requests.get(f'{domain}{endpoint}/{meme_id}', headers=headers)
    assert response.status_code == 404, 'Error in meme deleting process'


def test_get_all_meme(domain, authorize):
    headers, endpoint = {'Authorization': f'{authorize}'}, '/meme'
    response = requests.get(f'{domain}{endpoint}', headers=headers)
    assert any(map(lambda x: True if 'fun' in x['tags'] else False, response.json()['data'])),\
        'No mem(s) with tags FUN'
