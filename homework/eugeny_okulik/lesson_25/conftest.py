import json
import pytest
import requests


DOMAIN = 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope='function')
def domain():
    return DOMAIN


@pytest.fixture(scope='function')
def prepare_post(domain):
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
    post_id = requests.request(
        'POST',
        f'{domain}/posts',
        headers=my_headers,
        data=my_data
    ).json()['id']
    yield post_id
    requests.request('DELETE', f'{domain}/posts/{post_id}')
