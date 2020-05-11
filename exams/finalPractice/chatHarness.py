from chatClass import chatbot


def main():
    bot = chatbot()

    bot.menu()
    
    option = int(input("What menu action would you like to perform?"))
    print("If you would like to end the chat, type: quit")
    print(" ")

    while (True):
        greetingData = bot.getGreeting()
        responseData = bot.randomResponse()

        if (option == 1):
            bot.convoStart()
        elif (option == 2):
            exit("Thank you for your time!")
        else:
            print("Oops... this isn't right")


if __name__ == "__main__":
    main()