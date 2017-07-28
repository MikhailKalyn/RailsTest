import base64
import requests
import json



class Request:
    def __init__(self, base_url, user, password):
        self.__url = base_url
        self.__user = user
        self.__password = password
        self.__auth = self.__get_basic_authorization_credentials(self.__user, self.__password)
        self.__header = {'Content-Type': 'application/json', 'Authorization': self.__auth}

    @staticmethod
    def __get_basic_authorization_credentials(user, password):
        return 'Basic ' + str(base64.b64encode(bytes('%s:%s' % (user, password), 'utf-8')), 'ascii').strip()

    def __send_request(self, method, uri, data=None):
        if data is None:
            data = {}
        if method == 'GET':
            return requests.get(self.__url + uri, headers=self.__header)
        elif method == 'POST':
            return requests.post(self.__url + uri, headers=self.__header, data=bytes(json.dumps(data), 'utf-8'))