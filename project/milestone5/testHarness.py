from metaInfo import metaInfo
from timeInfo import timeInfo

def main():
    meta = metaInfo()
    time = timeInfo()

    while (True):
        metaData = meta.getMeta()
        timeData = time.getTimeSeries()

        meta.menu()
        option = int(input("What menu action would you like to perform?"))
        print(" ")

        if (option == 1):
            meta.getGeneralInfo(metaData)
            print(" ")
            print(" ")
        elif (option == 2):
            meta.getCurrencyInfo(metaData)
            print(" ")
            print(" ")
        elif (option == 3):
            meta.getMarketInfo(metaData)
            print(" ")
            print(" ")
        elif (option == 4):
            time.process()
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