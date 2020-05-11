# Q1
# A
print("********************Q1*********************")
for i in range(1, 13):
    print(i)

print("———————————————————————————————————————————")

# B
x = 0
while x <= 11: 
    x += 1
    print(x)
print("*******************************************")


# Q2
print(' ')
print("********************Q2*********************")
for i in range(1, 13):
    if (i % 2 != 0):
        print(i)
print("*******************************************")


# Q3
print(' ')
print("********************Q3*********************")
userInput = input("Enter some text: ")

sliced = str(userInput)[::-1]

print("Reversed: " + str(sliced))
print("*******************************************")


# Q4
print(' ')
print("********************Q4*********************")
password = input("Enter password: ")

'''
if (re.search('[a-zA-Z]', str(password)):
    print("Hello")
elif (re.search('[0-9]', str(password)):
    print("Hello")
elif ((("$" in str(password)) || ("#" in str(password)) || ("@" in str(password))):
    print("Hello")
'''
print("*******************************************")


# Q5
print(' ')
print("********************Q5*********************")
for i in range(1, 51):
    if ((i % 3 == 0) and (i % 5 == 0)):
        print("bizzbuzz")
    elif (i % 3 == 0):
        print("bizz")
    elif (i % 5 == 0):
        print("buzz")
    else:
        print(i)
print("*******************************************")