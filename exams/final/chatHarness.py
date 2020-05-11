from chatBot import chatbot

def main():
    chatBot = chatbot()

    chatBot.menu()
    
    option = int(input("What menu action would you like to perform?"))
    print("If you would like to end the chat, type: quit")
    print(" ")

    while(True):
        known = chatBot.createKnownResponses()
        random = chatBot.createUnknownResponses()
        unknown = chatBot.questionsToLearn()

        if (option == 1):
            chatBot.process(known, random, unknown)
        elif (option == 2):
            exit("Thank you for your time!")
        else:
            print("Please enter a valid option")


if __name__ == "__main__":
    main()