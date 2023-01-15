from requests import Response


class Endpoint:

    _response = None

    def __init__(self, response: Response):
        self._response = response

    @property
    def response_is_200(self) -> bool:
        return self._response.status_code == 200

    @property
    def response_is_404(self) -> bool:
        return self._response.status_code == 404

    @property
    def data(self):
        return self._response.json()
