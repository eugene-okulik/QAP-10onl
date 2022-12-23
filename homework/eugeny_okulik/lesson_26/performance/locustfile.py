from random import randint
from locust import task, HttpUser


class QuickStartUser(HttpUser):
    token = ''

    def on_start(self):
        response = self.client.post(
            '/authorize',
            json={'name': 'Vasia'}
        )
        self.token = response.json()['token']

    @task
    def get_memes(self):
        self.client.get(
            f'/meme/{randint(1, 3)}',
            headers={'Authorization': self.token}
        )

    @task
    def get_all_memes(self):
        self.client.get(
            '/meme/',
            headers={'Authorization': self.token}
        )
