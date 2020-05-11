import requests
import json

finance = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=ITMI469AL65D1CW8")

print(finance.status_code)

USD = json.loads(finance.text)

print(USD.keys())
print(USD['Meta Data'])
print(USD['Time Series (Digital Currency Daily)'])