import requests
from random import randint


def login(clientName=None, clientEmail=None):
    json = {
        'clientName': clientName,
        'clientEmail': clientEmail
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response


def get_token():
    nr = randint(1, 999999)
    json = {
        'clientName': 'Paula',
        'clientEmail': f'valid_email{nr}@email.com'
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response.json()['accessToken']
