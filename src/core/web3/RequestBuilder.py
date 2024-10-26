import requests
from requests import Request, PreparedRequest

from src.core.data.infura.RequestData import RequestData, BalanceRequest


class RequestBuilder():
    def __init__(self):
        pass

    def get_balance_request(self, address: str, api_key: str) -> PreparedRequest:
        get_balance_request: BalanceRequest = BalanceRequest(address=address)
        req = requests.Request(get_balance_request.request_type,
                               url=self.request_data.get_url(),
                               headers=self.request_data.headers,
                               json=get_balance_request.get_payload())

        return req.prepare()
