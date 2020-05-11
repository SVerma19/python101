import requests
import json

class metaInfo: 

    def __init__(self):
        self.rescponse = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=ITMI469AL65D1CW8")
        self.finance = json.loads(self.response.text)
        self.metaDictionary = {}

        ''' 
        print(finance)
        print(response.status_code)
        print("finance keys: ", finance.keys())
        print(finance['Meta Data'])
        print(finance['Time Series (Digital Currency Daily)'])
        '''


    def getMeta(self):  
        self.metaDictionary = self.finance.get('Meta Data')
        return self.metaDictionary


    def menu(self):
        print("Daily Prices and Volumes for Digital Currency")
        print("************************")
        print("1) Get general infromation")
        print("2) Get infromation about the currency")
        print("3) Get information about the market")
        print("4) Get information about the prices")
        print("5) Quit")
        print(" ")


    def getGeneralInfo(self, meta):
        print("************* General Information *************")
        print("Subject: ", self.metaDictionary.get('1. Information'))
        print("Last Refreshed: ", self.metaDictionary.get('6. Last Refreshed'))
        print("Time Zone: ", self.metaDictionary.get('7. Time Zone'))


    def getCurrencyInfo(self, meta):
        print("************* Digital Currency Infromation *************")
        print("Code: ", self.metaDictionary.get('2. Digital Currency Code'))
        print("Name: ", self.metaDictionary.get('3. Digital Currency Name'))


    def getMarketInfo(self, meta):
        print("************* Market Infromation *************")
        print("Code: ", self.metaDictionary.get('4. Market Code'))
        print("Name: ", self.metaDictionary.get('5. Market Name'))