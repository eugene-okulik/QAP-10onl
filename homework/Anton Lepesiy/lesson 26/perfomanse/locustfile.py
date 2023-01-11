from locust import task, HttpUser
from random import randint


class WQuickStartUser(HttpUser):
    token = ''

    def on_start(self):
        response = self.client.post(
            '/autorise',
            json={'name': 'Vasia'}
        )
        self.token = response.json()['token']

    @task
    def get_memes(self):
        self.client.get(
            f'/meme/{randint(1, 3)}',
            headers={'Autorization': self.token}
        )
