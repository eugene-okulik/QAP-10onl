from endpoints.add_meme import AddMeme


def test_add_valid_meme(auth):
    add_valid_meme = AddMeme(auth)
    assert add_valid_meme.response_is_200()
    assert add_valid_meme.added_text_is_correct()
