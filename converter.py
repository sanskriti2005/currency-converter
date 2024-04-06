import argparse
from configparser import ConfigParser
from urllib import parse, request
import json

BASE_API_URL = "https://api.exconvert.com/convert"

# FETCHES API KEY
def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["exconvert"]["api_key"]

# PARSES USER ARGUMENTS 
def read_user_cli_args():
    #description of what is needed from the user
    parser = argparse.ArgumentParser(
        description = "gets base_currency, the amount and returns the amount in the target currency"
    )

    #base_currency argument
    parser.add_argument(
        "base_currency", type = str, help="enter a currency."
    )


    #target_currency argument
    parser.add_argument(
        "target_currency", type=str, help="enter a target currency"
    )


    #amount argument
    parser.add_argument(
        "amount", type = int, help="enter an amount."
    )

    #currency_rate argument, is displayed based on the user's input (if they asked for it)
    parser.add_argument(
        "-c",
        "--currency_rate",
        action="store_true",
        help="display the currency rate"

    )
    return parser.parse_args()



#BUILD THE URL TO FETCH THE DATA 
def build_conversion_query(base_currency, target_currency, amount, currency_rate = False):
    #api_key
    api_key = _get_api_key

    #converting base_currency to url format
    base_currency_name = base_currency.upper()
    url_encoded_base_currency = parse.quote_plus(base_currency_name)

    #converting target_currency to url format 
    target_currency_name = target_currency.upper()
    url_encoded_target_currency = parse.quote_plus(target_currency_name)


    #the url
    url = f"{BASE_API_URL}?access_key={api_key}&from={base_currency_name}&to{target_currency_name}&{amount}"
    return url








if __name__ == "__main__":
    user_args = read_user_cli_args()
    query_url = build_conversion_query(user_args.base_currency, user_args.target_currency, user_args.amount, user_args.currency_rate)
    print(query_url)