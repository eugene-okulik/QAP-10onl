from urllib import request
import json
import domain as domain


def test_get_all_posts():
    req = request.Request('https://jsonplaceholder.typicode.com/posts')
    # response = request.urlopen(req).read().decode('utf-8')
    response = request.urlopen(req)
    response = json.load(response)
    # print(response[0]['title'])
    assert len(response) == 100


def test_get_one_post(domain):
    req = request.Request(f'{domain}/posts/11')
    response = json.load(request.urlopen(req))


def test_add_post(domain):
    req = request.Request(f'{domain}/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps(
        {
            "title": "QAP10 todays news",
            "body": "abra",
            "userId": "1"
        }
    ).encode('ascii')
    response = json.load(request.urlopen(req))
    print(response)
