import argparse
import os
from configparser import ConfigParser
from urllib import parse, request, error
import json
import sys
from pprint import pp 


BASE_API_URL = "https://api.exconvert.com/convert"


# FETCHES API KEY

def _get_api_key():
     return os.getenv("EXCONVERT_API_KEY")

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
    api_key = _get_api_key()

    #converting base_currency to url format
    base_currency_name = base_currency.upper()
    url_encoded_base_currency = parse.quote_plus(base_currency_name)

    #converting target_currency to url format 
    target_currency_name = target_currency.upper()
    url_encoded_target_currency = parse.quote_plus(target_currency_name)


    #the url
    url = (
        f"{BASE_API_URL}?from={base_currency_name}&to={target_currency_name}&amount={amount}&access_key={api_key}")


    return url



#GET DATA FROM THE URL
def get_conversion_data(query_url):

        #create a request object for the built url and include a user-agent
        req = request.Request(query_url, headers={'User-Agent': 'Mozilla/5.0'})

        try:
            #initiating the http request from the request object
            response = request.urlopen(req)

        #incase of an error    
        except error.HTTPError as http_error:
              #401 Unauthorized
            if http_error.code == 401:
                  sys.exit("Access Denied, Check your API key.")
             #401 Not-Found
            elif http_error.code == 404:
                  sys.exit("Can't find the data for the mentioned currency, our apologies.")
            else: 
                 sys.exit(f"Something went wrong... ({http_error.code})")
               
               

        #the data from the response is read
        data = response.read()

        #returns deserialised json into a python dictionary
        try:
            return json.loads(data)
        
        #unless.. there is an error (the horrors)
        except:
             sys.exit("Couldn't read the server response")


#DISPLAY INFOMRATION
def display_information(conversion_data, currency_rate=False):
    #base currency
    print(f"Base: {conversion_data['base']}")

    #target currency
    target_currency = list(conversion_data['result'].keys())[0]
    print(f"Target Currency: {target_currency}")

    #amount entered by the user
    print(f"Amount in base currency: {conversion_data['amount']}")

    #amount in target currency
    print(f"Converted Amount in Target Currency: {conversion_data['result'][target_currency]}")
    
    #if the user asks for the currency rate
    if currency_rate:
        print(f"Conversion Rate: {conversion_data['result']['rate']}")

     



if __name__ == "__main__":
    user_args = read_user_cli_args()
    query_url = build_conversion_query(user_args.base_currency, user_args.target_currency, user_args.amount, user_args.currency_rate)
    conversion_data = get_conversion_data(query_url)
    display_information(conversion_data, user_args.currency_rate)
    