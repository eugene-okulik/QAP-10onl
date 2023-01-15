from endpoints.delete_meme import DeleteMeme


def test_delete_meme(auth, add_meme1):
    delete_meme = DeleteMeme(auth, add_meme1)
    assert delete_meme.response_is_404()
