from math import pow

# Q1: String manipulation
print("*********Q1*********")

firstname = "Sam"
lastname = "Jones!"

print("Hello,", firstname, lastname, "You just delved into python.")
print("*********************")
print(" ")


# Q2: String manipulation using a function and string functions
print("*********Q2*********")
words = "A string with multiple words"

def split(words):
    splitWords = words.split(' ')
    return splitWords 
  
def join(words): 
    #joinWords = '-*-'.join(words)
    joinWords = words.replace(' ', '-*-')
    return joinWords

print("split string:", split(words))
print("joined string:", join(words))
print("*********************")
print(" ")


# Q3: Iterations and conditional logic
print("*********Q3*********")
n = 7

for i in range(0, n):
    print("original:", i, " ", "squared:", i**2)

print("*********************")
print(" ")


# Q4: Iterations and conditional logic
print("*********Q4*********")
year = int(input("enter a year:"))

'''
if (year % 400 == 0):
   if (year % 100 != 0):
       if (year % 4 == 0):
           print(bool(year))
       else:
           print(bool(year))
   else:
       print(bool(year))
else:
   print(bool(year))
'''

if (year % 4 == 0) and (year % 100 != 0):
    print(bool(year))
elif (year % 100 != 0):
    print(bool(year))
elif (year % 400 == 0):
    print(bool(year))
else:
    print("False")

print("*********************")
print(" ")


# Q5: Working with Dictionaries, Lists, and Functions
print("*********Q5*********")
strings = "silly sally sold silly sea shells on the sea shore. sally is so silly"
ss = strings.split()
dictionary = {}

for word in ss:
    count = ss.count(word)
    dictionary.update({word: count})
print(dictionary)

print("*********************")
print(" ")


# EC: Problem solving