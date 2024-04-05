import argparse
from configparser import ConfigParser
from urllib import request
import json

BASE_API_URL = "https://api.freecurrencyapi.com/v1/latest:"

# FETCHES API KEY
def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["freecurrencyapi"]["api_key"]

# PARSES USER ARGUMENTS 
def read_user_cli_args():
    parser = argparse.ArgumentParser(
        description = "gets base_currency, the amount and returns the amount in the target currency"
    )
    parser.add_argument(
        "base_currency", type = str, help="enter a currency."
    )
    parser.add_argument(
        "amount", type = int, help="enter an amount."
    )
    parser.add_argument(
        "target_currency", type=str, help="enter a target currency"
    )
    parser.add_argument(
        "-c",
        "--currency_rate",
        action="store_true",
        help="display the currency rate"

    )
    return parser.parse_args()

#BUILD THE URL TO FETCH THE DATA FROM THE API
def build_conversion_query(base_currency, target_currency):
    api_key = _get_api_key
    base_currency_name = base_currency.upper() 
    target_currency_name = target_currency.upper()
    url = f"{BASE_API_URL}?apikey={api_key}&currencies={base_currency_name}%2C{target_currency_name}"
    return url








if __name__ == "__main__":
    user_args = read_user_cli_args()
    query_url = build_conversion_query(user_args.base_currency, user_args.target_currency)
    print(query_url)