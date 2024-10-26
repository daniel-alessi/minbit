import json
import os

import requests
from appdirs import user_data_dir
from requests import PreparedRequest, Response

from src.core.data.AppData import AppData
import keyring

from src.core.web3.RequestBuilder import RequestBuilder


class RequestManager():

    def __init__(self):
        self.request_builder = RequestBuilder()

    def send_balance_request(self, address: str) -> Response:
        request: PreparedRequest = self.request_builder.get_balance_request(address=address, api_key=self.get_api_key())
        with requests.Session() as session:
            return session.send(request)

    def get_api_key(self) -> str:
        return keyring.get_password(AppData.APP_NAME, AppData.API_KEY_ALIAS)

    def set_api_key(self, api_key: str):
        keyring.set_password(service_name=AppData.APP_NAME,username=AppData.API_KEY_ALIAS,password=api_key)

