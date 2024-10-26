import requests
from requests import Request, PreparedRequest

from src.core.data.infura.RequestData import RequestData, GetBalanceRequest


class RequestBuilder():
    def __init__(self, api_key=None):
        self.request_data = RequestData(api_key=api_key)

    def query_balance_request(self) -> PreparedRequest:
        get_balance_request: GetBalanceRequest = GetBalanceRequest(address="asd")
        req = requests.Request("POST",
                               url=self.request_data.get_url(),
                               headers=self.request_data.headers,
                               json=get_balance_request.get_payload())

        return req.prepare()
