from configparser import ConfigParser

# FETCHES API KEY
def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["freecurrencyapi"]["api_key"]

