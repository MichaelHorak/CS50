import sys
import requests
import json

# Expects the user to specify as a command-line argument the number of Bitcoins,
# that they would like to buy. If that argument cannot be converted to a float,
# the program should exit via sys.exit with an error message.
# >> use sys argv

try:
    cl_arg = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

# Queries the API for the CoinDesk Bitcoin Price Index at
# https://api.coindesk.com/v1/bpi/currentprice.json
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Request exception")
# print(r.text)
res_json = r.json()
try:
    json_price = float(res_json["bpi"]["USD"]["rate_float"])
except ValueError:
    sys.exit("Error when converting json rate_float to float")

# print(json_price)

# python bitcoin.py 1
# which returns a JSON object, among whose nested keys is the current price of
# Bitcoin as a float.
# use requests.get & requests.json
# Be sure to catch any exceptions, as with code like:
# import requests
#
# try:
#     ...
# except requests.RequestException:
#     ...
amount = json_price * cl_arg
print(f"${amount:,.4f}")
# Outputs the current cost of Bitcoins in USD to four decimal places,
# using , as thousands separator.
