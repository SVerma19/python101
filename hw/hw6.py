# Options menu for user
def menu():
    print("ATM")
    print("************************")
    print("1) Balance")
    print("2) Make Deposit")
    print("3) Make Withdrawal")
    print("4) Quit")
    print(" ")

# Deposit
def deposit(toDeposit, balance):
    balance += toDeposit
    return balance

# Withdraw
def withdraw(toWithdraw, balance):
    balance -= toWithdraw
    return balance

# Prints the balance
def printBalance(balance):
    print("your balance is: ", balance)

def main():
    balance = 500

    while (True):
        menu()
        option = int(input("What menu action would you like to perform?"))
        print(" ")

        if (option == 1):
            printBalance(balance)
            print(" ")
        elif (option == 2):
            toDeposit = int(input("How much would you like to deposit?"))
            balance = deposit(toDeposit, balance)

            printBalance(balance)
            print(" ")
        elif (option == 3):
            toWithdraw = int(input("How much would you like to withdraw?"))
            balance = withdraw(toWithdraw, balance)

            printBalance(balance)
            print(" ")
        elif (option == 4):
            exit("Thank you for choosing this bank")
            print(" ")
        else:
            print("Not a valid entry")
            print(" ")

if __name__ == "__main__":
   main()