import argparse
from configparser import ConfigParser

# FETCHES API KEY
def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["freecurrencyapi"]["api_key"]

# 
def read_user_cli_args():
    parser = argparse.ArgumentParser(
        description = "gets currency and the target currency for conversion"
    )
    parser.add_argument(
        "currency", type = str, help="enter a currency."
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


if __name__ == "__main__":
    user_args = read_user_cli_args()
    print(user_args.currency, user_args.target_currency, user_args.currency_rate)