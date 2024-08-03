from typing import Dict, Optional


class Wallet():

    def __init__(self, alias: str , address: str, key: str) -> None:
        self.alias = alias
        self.address = address
        self.key = key

    def to_dict(self) -> dict[str, dict[str, str]]:
        return {
            self.alias: {"address": self.address}
        }

