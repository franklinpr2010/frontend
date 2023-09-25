import requests
from . import CARRINHO_API_URL
from flask import session


class CarrinhoClient:
    @staticmethod
    def get_carrinho():
        header = {'Authorization': session['user_api_key']}

        response = requests.get(CARRINHO_API_URL + '/api/carrinho', headers=header)
        print('get_carrinho')
        print(response.json())

        return response.json()

    @staticmethod
    def add_to_cart(produto_id, quantity=1):
        payload = {
            'produto_id': produto_id,
            'quantity': quantity
        }
        header = {'Authorization': session['user_api_key']}

        response = requests.post(CARRINHO_API_URL + '/api/carrinho/add-item',
                                 data=payload,
                                 headers=header)
        return response.json()

    @staticmethod
    def checkout():
        header = {'Authorization': session['user_api_key']}
        response = requests.post(CARRINHO_API_URL + '/api/carrinho/checkout', headers=header)
        return response.json()

    @staticmethod
    def get_carrinho_from_session():
        default_carrinho = {
            'items': {}
        }
        return session.get('carrinho', default_carrinho)
