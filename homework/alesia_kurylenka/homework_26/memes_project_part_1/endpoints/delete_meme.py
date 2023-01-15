from utils.send_request import send
from endpoints.endpoints_handler import Endpoint
import constants


class DeleteMeme(Endpoint):
    def __init__(self, auth, add_meme1):
        self.auth = auth
        self.add_meme1 = add_meme1
        self.delete_meme(self.auth, self.add_meme1)

    def delete_meme(self, auth, add_meme1):
        send(auth, 'DELETE', f'{constants.DOMAIN}/meme/{add_meme1}')
        response = send(auth, 'GET', f'{constants.DOMAIN}/meme/{add_meme1}')
        self.status_code = response.status_code
