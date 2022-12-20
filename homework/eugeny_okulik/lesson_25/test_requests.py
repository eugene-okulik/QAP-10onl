import json
import requests


def test_get_all_posts(domain):
    response = requests.request('GET', f'{domain}/posts').json()
    print(response)
    assert len(response) == 100


def test_get_one_post(domain):
    response = requests.request('GET', f'{domain}/posts/11').json()
    assert response['id'] == 11


def test_add_post(domain):
    my_headers = {
        'Content-Type': 'application/json',
        # 'Authorization': 'skjdhfksjdfhwieuyiwejhsf',
    }
    my_data = json.dumps(
        {
            "title": "QAP10 today's news",
            "body": (
                "asfslkdjfhaksjdfa dslkfjsfgkljas fkasjfdhlaskjdfhlka daklsdhfalskd sdfgsdfgsdf"
                " sdfgsdfg sdfgsdg fasdjkfnaksjdflas df asdlfjfaslkdfj"
            ),
            "userId": 1
        }
    )
    response = requests.request(
        'POST',
        f'{domain}/posts',
        headers=my_headers,
        data=my_data
    ).json()
    assert response['title'] == 'QAP10 today\'s news'


def test_update_post(domain, prepare_post):
    my_headers = {
        'Content-Type': 'application/json',
    }
    my_data = json.dumps(
        {
            "title": "QAP10 today's news- UPDATED",
            "body": (
                "asfslkdjfhaksjdfa dslkfjsfgkljas fkasjfdhlaskjdfhlka daklsdhfalskd sdfgsdfgsdf"
                " sdfgsdfg sdfgsdg fasdjkfnaksjdflas df asdlfjfaslkdfj"
            ),
            "userId": 1
        }
    )
    response = requests.request(
        'PUT',
        f'{domain}/posts/{prepare_post}',
        headers=my_headers,
        data=my_data
    ).json()
    assert response['title'] == 'QAP10 today\'s news- UPDATED'


def test_delete_post(domain, prepare_post):
    requests.request('DELETE', f'{domain}/posts/{prepare_post}')
    response = requests.request('GET', f'{domain}/posts/{prepare_post}')
    assert response.status_code == 404
