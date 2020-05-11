import requests
import json

def init():
    response = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=ITMI469AL65D1CW8")
    finance = json.loads(response.text)
    return finance

    ''' 
    print(finance)
    print(response.status_code)
    print("finance keys: ", finance.keys())
    print(finance['Meta Data'])
    print(finance['Time Series (Digital Currency Daily)'])
    '''


def getMeta(finance):  
    metaDictionary = finance.get('Meta Data')
    return metaDictionary


def getTimeSeries(finance):
    timeSeries = finance.get('Time Series (Digital Currency Daily)')
    return timeSeries


def menu():
    print("Daily Prices and Volumes for Digital Currency")
    print("************************")
    print("1) Get general infromation")
    print("2) Get infromation about the currency")
    print("3) Get information about the market")
    print("4) Get information about the prices")
    print("5) Quit")
    print(" ")


def getGeneralInfo(meta):
    print("************* General Information *************")
    print("Subject: ", meta.get('1. Information'))
    print("Last Refreshed: ", meta.get('6. Last Refreshed'))
    print("Time Zone: ", meta.get('7. Time Zone'))


def getCurrencyInfo(meta):
    print("************* Digital Currency Infromation *************")
    print("Code: ", meta.get('2. Digital Currency Code'))
    print("Name: ", meta.get('3. Digital Currency Name'))


def getMarketInfo(meta):
    print("************* Market Infromation *************")
    print("Code: ", meta.get('4. Market Code'))
    print("Name: ", meta.get('5. Market Name'))


# FIX THIS CLASS — ONlY BROKEN PART OF THE PROGRAM
def getPriceInfo(time):
    print("************* Price Infromation *************")
    user = input("Please select a date using the format YYYY-MM-DD:")
    z = time.get(user)
    print(z)

    user2 = input("Select what you would like to look at -- 1a. open (USD) -- 2a. high (USD) -- 3a. low (USD) -- 4a. close (USD) -- 5. volume -- 6. market cap (USD):")
    q = z.get(user2)
    print("Your selection---", user2, "---is:", q)


def main():
    while (True):
        d = init()
        meta = getMeta(d)
        time = getTimeSeries(d)
        menu()
        option = int(input("What menu action would you like to perform?"))
        print(" ")

        if (option == 1):
            getGeneralInfo(meta)
            print(" ")
            print(" ")
        elif (option == 2):
            getCurrencyInfo(meta)
            print(" ")
            print(" ")
        elif (option == 3):
            getMarketInfo(meta)
            print(" ")
            print(" ")
        elif (option == 4):
            getPriceInfo(time)
            print(" ")
            print(" ")
        elif (option == 5):
            exit("Thanks for your time!")
            print(" ")
            print(" ")
        else:
            print("Not a valid entry")
            print(" ")
            print(" ")

if __name__ == "__main__":
   main()