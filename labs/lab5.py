import collections

# DICTIONARY TESTER
dictionary = {
    "player": "Tom Brady",
    "team": "NE Patriots",
    "position": "Quarterback"
}

print(dictionary)
print("**********************")

print(dictionary["team"])
print("**********************")

if "team" in dictionary:
    print("true")
else:
    print("false")
print("**********************")

dictTwo = dictionary.copy()
print("original dictionary: ", dictionary)
print("second dictionary: ", dictTwo)
print("**********************")

dictionary.clear()
print("empty dictionary: ", dictionary)
print("**********************")


# FREQUENCY COUNTER
words = "I am Sam, sam I am. that Sam I am, that Sam I am, I do not like that Sam I am"
ws = words.split()
wordDict = {}

for word in ws:
    count = ws.count(word)
    wordDict.update({word: count})
print(wordDict)

'''
c = collections.Counter(words.split())
print(c)
'''