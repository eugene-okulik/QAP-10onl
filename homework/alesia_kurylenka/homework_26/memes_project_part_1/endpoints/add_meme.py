from utils.send_request import send
from endpoints.endpoints_handler import Endpoint
import constants


class AddMeme(Endpoint):
    def __init__(self, auth):
        self.auth = auth
        self.add_meme(self.auth)

    def add_meme(self, auth):
        body = (
            {
                "text": 'you are very boring, but you can continue',
                "url": "http://risovach.ru/upload/2019/06/mem/kapibara-odobryaet_211465163_orig_.jpg",
                "tags": ["capybara", "meme", "fun"],
                "info": {
                    "colors": [
                        "brown",
                        "red",
                        "white"
                    ],
                    "objects": [
                        "picture",
                        "text"
                    ]
                }
            }
        )
        response = send(auth, 'POST', f'{constants.DOMAIN}/meme', body)
        self.status_code = response.status_code
        if 'text' not in response.json():
            self.response_body = response.json()[0]
        else:
            self.response_body = response.json()
        return self.response_body

    def added_text_is_correct(self) -> bool:
        return self.response_body['text'] == 'you are very boring, but you can continue'
