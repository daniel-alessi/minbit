from src.core.data.WalletHandler import WalletHandler


class MinBit():
    def __init__(self):
        pass

    def make_wallet(self, alias: str, address: str, key: str ):

        WalletHandler().add_wallet( alias=alias, address=address, key=key)

    def list_wallet(self, explicit:bool=False):

        for wallet in WalletHandler().list_wallets(explicit=explicit):
            print(wallet)

