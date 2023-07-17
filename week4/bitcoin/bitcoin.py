import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    resquest = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") # CoinDesk API
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    data = resquest.json()
    bpi = data["bpi"]
    usd = bpi["USD"]
    price = usd["rate"]
    price = price.replace(",", "")
    price = float(price) * float(sys.argv[1])
    print(f"${price:,.4f}")
