import requests
from flask import Blueprint, jsonify, request, make_response, session
from . import USER_API_URL



class UserClient:
    @staticmethod
    def login(form):
        api_key = None
        payload = {
            'username': form.username.data,
            'password': form.password.data
        }

        url = USER_API_URL + '/api/user/login'

        response = requests.post(url, data=payload)
        if response:
            api_key = response.json().get('api_key')

        return api_key

    @staticmethod
    def get_user():
        headers = {
            'Authorization': session['user_api_key']
        }

        url = USER_API_URL + '/api/user'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def create_user(form):
        user = None
        payload = {
            'password': form.password.data,
            'username': form.username.data,
            'cep': form.cep.data
        }
        url = USER_API_URL + '/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        return response

    @staticmethod
    def user_exists(username):
        url = USER_API_URL + '/api/user/' + username + '/exists'

        response = requests.get(url)
        return response.status_code == 200
