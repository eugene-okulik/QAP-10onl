
def test_add_meme(client):
    test_text = 'Best meme generator'
    add_result = client.add_meme(test_text)
    client.delete_mem(add_result['id'])
    assert add_result['text'] == test_text


def test_update_meme(client, add_meme):
    update_result = client.update_meme(add_meme['id'])
    assert update_result['text'] == 'Memes Everywhere'


def test_delete_meme(client):
    test_text = 'Best meme generator'
    add_result = client.add_meme(test_text)
    delete_result = client.delete_mem(add_result['id'])
    assert delete_result.response_is_200


def test_get_all_memes(client):
    get_result = client.get_all_memes()
    assert get_result
