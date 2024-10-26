from src.core.wallet.WalletHandler import WalletHandler


class MinBit():
    def __init__(self):
        self.wallet_handler = WalletHandler()
        pass

    def make_wallet(self, alias: str, address: str, key: str ):

        self.wallet_handler.add_wallet( alias=alias, address=address, key=key)

    def list_wallet(self, explicit:bool=False):

        for wallet in self.wallet_handler.list_wallets(explicit=explicit):
            print(wallet)

    def look(self, address: str):

        print(f"look: {address}")
        pass

