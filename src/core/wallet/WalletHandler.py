import os
import json
from appdirs import user_data_dir
from typing import Dict, List
import keyring
from src.core.data.AppData import AppData
from src.core.data.wallet.Wallet import Wallet


class WalletHandler():

    def __init__(self):

        self.data_dir = user_data_dir(AppData.APP_NAME)
        self.data_file = os.path.join(self.data_dir, AppData.WALLET_FILE_NAME)
        self.default_wallet_data = {}
        self.wallet_data = self._load_data()

    def list_wallets(self, explicit:bool=False) -> List[Wallet]:

        return [self.get_wallet(alias, explicit=explicit) for alias in self.wallet_data.keys()]

    def get_wallet(self, alias: str, explicit: bool = False) -> Wallet:

        if explicit:
            return Wallet(json=self.wallet_data.get(alias), key=keyring.get_password(AppData.APP_NAME, alias))
        return Wallet(json=self.wallet_data.get(alias))

    def add_wallet(self, alias: str, address: str, key: str):

        if self._check_alias_exists(alias):
            raise IOError("wallet already exists")

        keyring.set_password(service_name=AppData.APP_NAME, username=alias, password=key)
        wallet = Wallet(alias=alias, address=address, key=key)
        self.wallet_data[alias] = (wallet.to_dict())
        self._save_data()
        self._refresh_data()

    def remove_wallet(self, alias: str):

        if not self._check_alias_exists(alias):
            raise IOError("wallet doesnt exists")

        keyring.delete_password(service_name=AppData.APP_NAME, username=alias)
        self.wallet_data.pop(alias)
        self._save_data()
        self._refresh_data()

    def _load_data(self) -> Dict:
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                json_data = json.load(f)
                f.close()
                return json_data

        os.makedirs(self.data_dir, exist_ok=True)
        return self.default_wallet_data

    def _refresh_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.wallet_data = json.load(f)
                f.close()
        else:
            self.wallet_data = self.default_wallet_data

    def _save_data(self) -> None:
        with open(self.data_file, 'w') as f:
            json.dump(self.wallet_data, f, indent=4)
            f.close()

    def _check_alias_exists(self, alias: str) -> bool:
        if alias in self.wallet_data:
            return True
        return False
