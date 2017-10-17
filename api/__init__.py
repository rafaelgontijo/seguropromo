from django.conf import settings
import base64
import json
import requests


class Api(object):
    """ Object from abstract calls of api """
    base_url = settings.SEGUROSPROMO_URL

    def __init__(self):
        username = settings.SEGUROSPROMO_USER
        password = settings.SEGUROSPROMO_PASS
        token = base64.b64encode(str.encode(
            "{}:{}".format(username, password))).decode()
        authorization = "Basic {}".format(token)
        self.headers = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Charset": "utf-8"
        }

    def get(self, url):
        """ Method to list object """
        response = requests.get(
            url=url,
            headers=self.headers
        )
        return response.json()

    def post(self, url, body):
        """ Method to create a object """
        response = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(body)
        )
        return response.json()
