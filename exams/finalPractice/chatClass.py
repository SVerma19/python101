import random

class chatbot:
    
    def __init__(self):
        self.greetingDictionary = {}
        self.responseDictionary = {}


    def getGreeting(self):

        self.greetingDictionary = {
            'hey': "Hello there!",
            'hi': "Howdy!",
            'hello': "Greetings human",
            'help': "What can I help you with?",
            'weather': "Cloudy with a chance of meatballs",
        }

        '''
        self.greetingDictionary[('Hello', 'Hi', 'Hey', 'Greetings', 'Sup')] = 'Hello there!'
        self.greetingDictionary[('Help', 'Assistance', 'Looking', 'Searching')] = 'What can I help you with?'
        
        
        self.greetingDictionary = {
            "Hello there!": ('Hello', 'Hi', 'Hey', 'Greetings', 'Sup'),
            "What can I help you with?": ('Help', 'Assistance', 'Looking', 'Searching'),
        }
        '''
        return self.greetingDictionary


    def randomResponse(self):
        self.randomList = ["I'm not sure what you are saying", "Can you rephrase your question", "I'm sorry, I didn't quite get that"]
        return self.randomList


    def convoStart(self):
        self.sentence = str(input("You: "))
        word = self.sentence.lower().split()
        wordList = (word)

        keywords = self.greetingDictionary.keys()

        ''' 
        print(wordList)
        print(self.greetingDictionary)
        print(self.greetingDictionary.keys())
        print(self.greetingDictionary.values ())
        print(" ")
        '''


        for i in wordList:    
            if i == "quit" or i == "Quit":
                exit("Thank you for your time!")  
                print(" ")    
            elif i in self.greetingDictionary.keys():
                print("Bot:", self.greetingDictionary[i])
                print(" ")
                break       
            elif i not in self.greetingDictionary.keys():
                print("Bot:", random.choice(self.randomList))
                print(" ") 


    def menu(self):
        print("Welcome to your personal chat bot")
        print("************************")
        print("1) Talk to me")
        print("2) Exit")
        print(" ")           