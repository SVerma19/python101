import random

randomNum = random.randint(1, 99)
userNum = int(input("Guess a number: "))
guessCount = 4

while (int(guessCount) > 0):
    userNum = int(input("Guess a number: "))

    if (int(userNum) != int(randomNum)):
        guessCount -= 1
    if (int(userNum) == int(randomNum)):
        print("winner winner chicken dinner")
        break
    if (int(guessCount) == 0):
        print("sorry, try again")
        print("the number was:", int(randomNum))
        break



