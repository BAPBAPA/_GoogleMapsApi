import requests
from src.url_creating import *
from src.sources import *


class FullLifeCycle:

    @staticmethod
    def post():
        response = requests.post(url=post_url_creating(), json=POST_BODY)

        return response

    @staticmethod
    def get(place_id):
        response = requests.get(url=get_url_creating(), params={'place_id': place_id})

        return response

    @staticmethod
    def put(place_id):
        put_body = {'place_id': place_id}
        put_body.update(PUT_BODY)

        response = requests.put(url=put_url_creating(), json=put_body)

        return response

    @staticmethod
    def delete(place_id):
        response = requests.delete(url=delete_url_creating(), json={'place_id': place_id})

        return response
