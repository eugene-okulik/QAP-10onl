from utils.send_request import send
from endpoints.endpoints_handler import Endpoint
import constants


class GetAllMemes(Endpoint):
    def __init__(self, auth):
        self.auth = auth
        self.get_all_memes(self.auth)

    def get_all_memes(self, auth):
        response = send(auth, 'GET', f'{constants.DOMAIN}/meme')
        self.status_code = response.status_code
        if self.status_code == 200:
            self.response_body = response.json()
        else:
            self.response_body = response.text

    def check_fun_in_tags(self):
        fun_tags_count = 0
        for meme in self.response_body['data']:
            if 'fun' in meme['tags']:
                fun_tags_count += 1
        return fun_tags_count
