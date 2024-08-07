from typing import Dict, Optional, Set


class Wallet():

    def __init__(self, alias: str , address: str, key: str) -> None:
        self.alias = alias
        self.address = address
        self.key = key

    def to_dict(self) -> dict[str, str]:
        return {
                 "address": self.address,
                 "alias": self.alias
        }

    def __str__(self) -> str:
        return f"Alias: {self.alias}, Address: {self.address}, Key: {self.key}"

