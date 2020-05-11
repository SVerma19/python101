import random

class chatbot:
    
    def __init__(self):
        self.keywordResponses = {}
        self.randomResponses = []
        self.logList = []
        self.unansweredQuestions = []


    def menu(self):
        print("I am CHATBOT. Can I help you?")
        print("***************")
        print("1) Talk to me")
        print("2) Nah, I'm good")
        print(" ")    


    def createKnownResponses(self):
        self.keywordResponses = {
            'hey': "Hey, what's up?",
            'hi': "Hi! How are you?",
            'hello': "Hello",
            'football': "The Patriots are still the best team in the league, don't listen to everyone else.",
            'local': "Fairfield, CT is experiencing normal town stuff.",
            'university': "I've heard that Fairfield University isn't bad.",
            'usa': "Donald Trump is actually facing impeachment. See you in the history books in 40 years.",
            'technology': "Lots of new things happening in the technology world. I've heard that AI is improving everyday, especially whenchatboxes.",
        }
        return self.keywordResponses


    def createUnknownResponses(self):
        self.randomResponses = [
            "I'm not quite sure what you mean, can you please rephrase your question?", 
            "Sorry, I can't help you with that specific request",
            "We have the best selection and prices, for more information check out our website or call a representative.", 
            "I don't think I can help you with that. For more assistance call our customer service hotline (p.s. it'll probably jut be another computer automation).",
        ]
        return self.randomResponses

    
    #PROBLEM — NOT READING FULL SENTENCE BEFORE SPITTING OUT RESPONSE
    def process(self, keywordResponses, unknownResponses, unansweredQuestions):
        count = 0

        while(True):
            count += 1

            self.customer = str(input("You: "))
            self.logList.append(self.customer)
            statement = self.customer.lower().split()
            split = (statement)
            
            for i in split:
                if i in self.keywordResponses.keys():
                    k = self.keywordResponses[i]
                    print("Bot: ", k)
                    print(" ") 

                    self.logList.append(k)
                    self.logList.append(" ")
                    break
                elif i == "quit" or i == "Quit":
                    self.runReport()
                    print(" ")

                    print("********** Number of Questions Asked **********") 
                    print("Total: ", count) #PROBLEM — Couldn't get the count in another method and have it get the correct amount of questions
                    
                    exit()
                    break
                else:
                    r = random.choice(self.randomResponses)
                    print(r)
                    print(" ")

                    self.logList.append(r)
                    self.unansweredQuestions.append(self.customer)
                    self.logList.append(" ")
                    break
                    print(" ") 

    
    def logHistory(self):
        self.logList =[]
        return self.logList


    def printLog(self):
        for i in self.logList:
            print(i)


    def questionsToLearn(self):
        self.unansweredQuestions = []

        #PROBLEM — Wasn't running with this code, but I believe with a proper directory for the open() it should save the answered questions to it
        '''
        with open('questionsToLearn.txt') as q:
            for i in self.unansweredQuestions:
                q.write("%s\n" % i)

        return self.unansweredQuestions
        '''

    def printUnanswered(self):
        for i in self.unansweredQuestions:
            print(i)


    def runReport(self):
        print("Bot: Thank you for your time! Here is a transcript of our interaction:")
        print(" ")
        print("********** Transcript **********")
        self.printLog()
        print(" ")
        print("********** Unanswered Questions **********")
        self.printUnanswered() 