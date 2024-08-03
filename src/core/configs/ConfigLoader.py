import os
import json
from appdirs import user_data_dir
from typing import Dict

from src.core.data.Wallet import Wallet

APP_NAME = "minbit"
data_dir = user_data_dir(APP_NAME)
os.makedirs(data_dir, exist_ok=True)
DATA_FILE = os.path.join(data_dir, "user_data.json")
WALLET_KEY = "wallets"
DEFAULT_WALLET_DATA = {WALLET_KEY: []}


def load_data() -> Dict:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_WALLET_DATA


def save_data(data) -> None:
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def add_wallet(wallet: Wallet) -> None:
    #add code here to store the wallet key

    data = load_data()
    if check_wallet_alias(data, wallet):
        raise IOError("wallet already exists")
    data[WALLET_KEY].append(wallet.to_dict())
    save_data(data)


def remove_wallet(wallet: Wallet) -> None:
    #add code here to remove the wallet key

    data = load_data()
    if not check_wallet_alias(data, wallet):
        raise IOError("wallet does not exist")
    data[WALLET_KEY].remove(wallet.to_dict())
    save_data(data)


def check_wallet_alias(data, wallet) -> bool:
    for existing_wallet in data["wallets"]:
        if wallet.alias in existing_wallet.keys():
            return True
    return False


wallet = Wallet(alias="wallet_alias",
                address="wallet_address",
                key="wallet_private_key")

add_wallet(wallet)
data = load_data()
print(data)
remove_wallet(wallet)
data = load_data()
print(data)
