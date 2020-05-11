import requests
import json

response = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=ITMI469AL65D1CW8")
finance = json.loads(response.text)

''' 
print(finance)
print(response.status_code)
print("finance keys: ", finance.keys())
print(finance['Meta Data'])
print(finance['Time Series (Digital Currency Daily)'])
'''

metaDictionary = finance.get('Meta Data')

def menu():
    print("Daily Prices and Volumes for Digital Currency")
    print("************************")
    print("1) Get general infromation")
    print("2) Get infromation about the currency")
    print("3) Get information about the market")
    print("4) Quit")
    print(" ")

def getGeneralInfo(finance):
    print("************* General Information *************")
    print("Subject: ", metaDictionary.get('1. Information'))
    print("Last Refreshed: ", metaDictionary.get('6. Last Refreshed'))
    print("Time Zone: ", metaDictionary.get('7. Time Zone'))

def getCurrencyInfo(finance):
    print("************* Digital Currency Infromation *************")
    print("Code: ", metaDictionary.get('2. Digital Currency Code'))
    print("Name: ", metaDictionary.get('3. Digital Currency Name'))

def getMarketInfo(finance):
    print("************* Market Infromation *************")
    print("Code: ", metaDictionary.get('4. Market Code'))
    print("Name: ", metaDictionary.get('5. Market Name'))

def main():
    while (True):
        menu()
        option = int(input("What menu action would you like to perform?"))
        print(" ")

        if (option == 1):
            getGeneralInfo(finance)
            print(" ")
            print(" ")
        elif (option == 2):
            getCurrencyInfo(finance)
            print(" ")
            print(" ")
        elif (option == 3):
            getMarketInfo(finance)
            print(" ")
            print(" ")
        elif (option == 4):
            exit("Thanks for your time!")
            print(" ")
            print(" ")
        else:
            print("Not a valid entry")
            print(" ")
            print(" ")

if __name__ == "__main__":
   main()