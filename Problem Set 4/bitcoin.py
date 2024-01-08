import sys
import requests
import json

if (len(sys.argv) != 2):
    sys.exit("Missing command-line argurment")
if(sys.argv[1].isalpha()):
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = float(o["bpi"]["USD"]["rate_float"])

    amount = rate * float(sys.argv[1])
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit("Request Exception")

