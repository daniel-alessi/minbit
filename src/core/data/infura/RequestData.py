# https://docs.infura.io/api/networks/ethereum/json-rpc-methods/eth_getbalance
from dataclasses import dataclass


@dataclass
class RequestData:
    url:str = "https://mainnet.infura.io/v3/"
    headers = {
        "Content-Type": "application/json"
    }

    def get_url(self, api_key: str) -> str:
        return self.url + api_key

@dataclass
class BalanceRequest:
    request_type:str = "POST"
    jsonrpc: str = "2.0"
    method: str = "eth_getBalance"
    address: str = None
    block: str = "latest"
    id: int = 1

    def get_payload(self) -> dict[str,str]:
        return {
            "jsonrpc": self.jsonrpc,
            "method": self.method,
            "params": [self.address, self.block],
            "id": self.id
        }



