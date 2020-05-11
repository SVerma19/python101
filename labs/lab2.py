# Q1
print("********************Q1*********************")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

product = int(num1) * int(num2)

print("The result is " + str(product))
print("*******************************************")


# Q2
print(' ')
print("********************Q2*********************")
userString = input("Enter a word: ")

stringLength = len(userString)

print("The length of the string is: " + str(stringLength))
print("*******************************************")


# Q3
print(' ')
print("********************Q3*********************")
userAge = input("Enter your age: ")

userAge10 = int(userAge) + 10

print("In 10 years, you'll be " + str(userAge10) + " years old")
print("*******************************************")


# Q4
print(' ')
print("********************Q4*********************")
userString2 = input("Enter a word: ")

firstCharacter = str(userString2)[:1]
lastCharacter = str(userString2)[-1:]

print(str(userString2))
print(str(firstCharacter) + ', ' + str(lastCharacter))
print("*******************************************")


# Q5
print(' ')
print("********************Q5*********************")
myString = "!!!"

print(myString * 10)
print("*******************************************")


# Q6
print(' ')
print("********************Q6*********************")
num3 = input("Enter a number: ")

if (int(num3) % 2 == 0):
    print(str(num3) + " is even")
if (int(num3) % 2 != 0):
    print(str(num3) + " is odd")
print("*******************************************")