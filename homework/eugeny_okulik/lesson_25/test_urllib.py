import json
from urllib import request, error


def test_get_all_posts(domain):
    req = request.Request(f'{domain}/posts')
    # response = request.urlopen(req).read().decode('utf-8')
    response = request.urlopen(req)
    response = json.load(response)
    # print(response[0]['title'])
    assert len(response) == 100


def test_get_one_post(domain):
    post_id = 11
    req = request.Request(f'{domain}/posts/{post_id}')
    response = json.load(request.urlopen(req))
    assert response['id'] == post_id


def test_add_post(domain):
    req = request.Request(f'{domain}/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    # req.add_header('Authorization', 'lakjsdhflkajsdhfadsafdlkjhf')
    req.data = json.dumps(
        {
            "title": "QAP10 today's news",
            "body": (
                "asfslkdjfhaksjdfa dslkfjsfgkljas fkasjfdhlaskjdfhlka daklsdhfalskd sdfgsdfgsdf"
                " sdfgsdfg sdfgsdg fasdjkfnaksjdflas df asdlfjfaslkdfj"
            ),
            "userId": 1
        }
    ).encode('ascii')
    response = json.load(request.urlopen(req))
    assert response['title'] == 'QAP10 today\'s news'


def test_update_post(domain):
    req = request.Request(f'{domain}/posts/11')
    req.method = 'PUT'
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps(
        {
            "title": "QAP10 today's news",
            "body": (
                "asfslkdjfhaksjdfa dslkfjsfgkljas fkasjfdhlaskjdfhlka daklsdhfalskd sdfgsdfgsdf"
                " sdfgsdfg sdfgsdg fasdjkfnaksjdflas df asdlfjfaslkdfj"
            ),
            "userId": 1
        }
    ).encode('ascii')
    response = json.load(request.urlopen(req))
    assert response['title'] == 'QAP10 today\'s news'


def test_delete_post(domain):
    req = request.Request(f'{domain}/posts/101', method='DELETE')
    json.load(request.urlopen(req))
    req = request.Request(f'{domain}/posts/101')
    try:
        json.load(request.urlopen(req))
    except error.HTTPError as err:
        assert err.code == 404
        return
    assert False, 'Post is not deleted'
