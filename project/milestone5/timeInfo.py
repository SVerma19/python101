import requests
import json

class timeInfo: 

    def __init__(self):
        self.response = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=ITMI469AL65D1CW8")
        self.finance = json.loads(self.response.text)
        self.timeSeries = {}

        ''' 
        print(finance)
        print(response.status_code)
        print("finance keys: ", finance.keys())
        print(finance['Meta Data'])
        print(finance['Time Series (Digital Currency Daily)'])
        '''


    def getTimeSeries(self):
        self.timeSeries = self.finance.get('Time Series (Digital Currency Daily)')
        return self.timeSeries


    def process(self):
        while (True):
            print("************* Price Infromation *************")    
            z = input("Please select a date using the format YYYY-MM-DD: ")
            date = self.timeSeries.get(z)
            print(date)
            print(" ")
            self.exitOption()


    def menu3(self):
        print("1) Select another date")
        print("2) Exit")
        print(" ")


    def exitOption(self):
        self.menu3()

        option = int(input("What menu action would you like to perform?"))
        print(" ")

        if (option == 1):
            self.process()
            print(" ")
            print(" ")
        elif (option == 2):
            exit("Thanks for your time!")
            print(" ")
            print(" ")


    '''
    def menu2(self):
        print("1) Open (USD)")
        print("2) High (USD)")
        print("3) Low (USD)")
        print("4) Close (USD)")
        print("5) Volume")
        print("6) Market Cap (USD)") 
        print("7) Quit")  
        print(" ")
  
 
    def getOpen(self):
        print("Open (USD): ", self.timeSeries.get('1a. open (USD)'))
    
    def getHigh(self):
        print("High (USD): ", self.timeSeries.get('2a. high (USD)'))

    def getLow(self):
        print("Low (USD): ", self.timeSeries.get('3a. low (USD)'))

    def getClose(self):
        print("Close (USD): ", self.timeSeries.get("4a. close (USD)"))

    def getVolume(self):
        print("Volume: ", self.timeSeries.get("5. volume"))

    def getMarketCap(self):
        print("Market Cap (USD): ", self.timeSeries.get("6. market cap (USD)"))


    def process()
        print(" ")
        self.menu2()
        option = int(input("What information would you like to view about the date?"))
        print(" ")

        if (option == 1):
            getOpen(self.date)
            print(" ")
            print(" ")
        elif (option == 2):
            date.getHigh(timeData)
            print(" ")
            print(" ")
        elif (option == 3):
            date.getLow(timeData)
            print(" ")
            print(" ")
        elif (option == 4):
            date.getClose(timeData)
            print(" ")
            print(" ")
        elif (option == 5):
            date.getVolume(timeData)
            print(" ")
            print(" ")
        elif (option == 6):
            date.getMarketCap(timeData)
            print(" ")
            print(" ")
        elif (option == 7):
            exit("Thanks for your time!")
            print(" ")
            print(" ")
        else:
            print("Not a valid entry")
            print(" ")
            print(" ")
    '''