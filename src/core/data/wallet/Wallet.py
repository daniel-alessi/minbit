from typing import Dict, Optional, Set


class Wallet():

    def __init__(self, key: str = '----', alias: str = None, address: str = None, json: Dict = None) -> None:
        self.alias = alias
        self.address = address
        self.key = key

        if json is not None:
            self.alias = json.get('alias')
            self.address = json.get('address')

    def to_dict(self) -> dict[str, str]:
        return {
            "address": self.address,
            "alias": self.alias
        }

    def __str__(self) -> str:
        return f"Alias: {self.alias}, Address: {self.address}, Key: {self.key}"

    __repr__ = __str__

