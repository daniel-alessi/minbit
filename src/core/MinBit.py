from src.core.data.WalletHandler import WalletHandler


class MinBit():
    def __init__(self):
        pass

    def make_wallet(self, alias: str, address: str, key: str ):

        wallet_handler = WalletHandler()
        wallet_handler.add_wallet(alias=alias, address=address, key=key)

