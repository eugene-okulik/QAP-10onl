from endpoints.update_meme import UpdateMeme


def test_update_meme(auth, add_meme1):
    update_meme = UpdateMeme(auth, add_meme1)
    assert update_meme.response_is_200()
    assert update_meme.updated_text_is_correct()
