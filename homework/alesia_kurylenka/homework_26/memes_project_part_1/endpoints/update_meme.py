from utils.send_request import send
from endpoints.endpoints_handler import Endpoint
import constants


class UpdateMeme(Endpoint):
    def __init__(self, auth, add_meme1):
        self.auth = auth
        self.add_meme1 = add_meme1
        self.update_meme(self.auth, self.add_meme1)

    def update_meme(self, auth, add_meme1):
        body = (
            {
                "id": add_meme1,
                "text": 'you are very boring, but you can continue updated',
                "url": "http://risovach.ru/upload/2019/06/mem/kapibara-odobryaet_211465163_orig_.jpg",
                "tags": [
                    "capybara",
                    "meme"
                ],
                "info": {
                    "colors": [
                        "brown",
                        "red"
                    ],
                    "objects": [
                        "picture",
                        "text"
                    ]
                }
            }
        )
        response = send(auth, 'PUT', f'{constants.DOMAIN}/meme/{add_meme1}', body)
        self.status_code = response.status_code
        if 'text' not in response.json():
            self.response_body = response.json()[0]
        else:
            self.response_body = response.json()
        return self.response_body

    def updated_text_is_correct(self) -> bool:
        return self.response_body['text'] == 'you are very boring, but you can continue updated'
