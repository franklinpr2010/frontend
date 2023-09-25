import requests

from . import PRODUTO_API_URL


class ProdutoClient:
    @staticmethod
    def get_produtos():
        response = requests.get(PRODUTO_API_URL + '/api/produtos/all')
        return response.json()

    @staticmethod
    def get_produto(slug):
        response = requests.get(PRODUTO_API_URL + '/api/produtos/' + slug)
        return response.json()
    
    
