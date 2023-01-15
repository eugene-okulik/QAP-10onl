from utils.send_request import send
import constants


class ApiClient:
    _token: str

    def __init__(self):
        self._token = ApiClient._authorize()

    @staticmethod
    def _authorize():
        headers = {
            'Content-Type': 'application/json'
            }
        body = {
            "name": "user"
            }

        response = send('', 'POST', f'{constants.DOMAIN}/authorize', body, headers)
        token = response.data['token']
        return token

    def add_meme(self, text):
        body = {
            "text": f"{text}",
            "url": "https://www.bouncegeek.com/wp-content/uploads/2017/10/Best-meme-generator-min.jpg",
            "tags": ["look"],
            "info": {"type": "png"}
            }
        response = send(self._token, 'POST', f'{constants.DOMAIN}/meme', body)
        return {"id": response.data['id'], "text": response.data['text']}

    def update_meme(self, meme_id):
        body = {
            "id": meme_id,
            "text": "Memes Everywhere",
            "url": "http://4.bp.blogspot.com/-EBM213mALjM/VSUKoz_t0CI/AAAAAAAAuKs/xf5lgQll82k/s1600/meme%2B(2).jpg",
            "tags": ["everywhere"],
            "info": {"type": "png"}
            }
        response = send(self._token, "PUT", f'{constants.DOMAIN}/meme/{meme_id}', body)
        return {"id": response.data['id'], "text": response.data['text']}

    def delete_mem(self, meme_id):
        response = send(self._token, 'DELETE', f'{constants.DOMAIN}/meme/{meme_id}')
        return response

    def get_all_memes(self):
        response = send(self._token, "GET", f'{constants.DOMAIN}/meme').data['data']
        test_result = False
        for mem in response:
            for tag in mem["tags"]:
                if 'fun' in tag:
                    test_result = True
                    break
        return test_result
