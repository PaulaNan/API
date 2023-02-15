from books.requests.api_client import *
from random import randint


class TestApiClient:
    nr = randint(1, 999999)
    clientName = 'Paula'
    clientEmail = f'valid_email{nr}@email.com'
    response = login(clientName, clientEmail)

    def test_login_200(self):
        assert self.response.status_code == 201, 'status code is not ok'

    def trest_login_has_token(self):
        assert 'access token' in self.response.json().keys(), 'token key is not present'

    def test_login_409(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'status code is not ok'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.', 'existing user message not ok'                                                                                                   'ok '

    def test_invalid_email(self):
        self.response = login('Paula', 'abc')
        assert self.response.status_code == 400, 'status code is not ok'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'invalid email message is not ok'
