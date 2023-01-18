from endpoints.get_all_memes import GetAllMemes


def test_get_all_meme(auth):
    memes_info = GetAllMemes(auth)
    assert memes_info.response_is_200()
    assert memes_info.check_fun_in_tags() > 0, "no memes with fun tag"
