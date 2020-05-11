candyCount = 5
candyList = []

while (int(candyCount) > 0):
    candy = input("Enter a candy: ")
    candyCount -= 1
    candyList.append(candy)
    listCount = candyList.count

print(" ")
print("number of elements in the list: ", len(candyList))

print(" ")
print("the list consists of: ")
print(*candyList, sep = ", ")

print(" ")
removeCandy = input("Enter a candy to remove from the list: ")
candyList.remove(removeCandy)

print(" ")
addCandy = input("Enter a new candy to add from the list: ")
candyList.insert(0, addCandy)

print(" ")
print("the new list consists of: ")
print(*candyList, sep = ", ")

print(" ")
candyList.sort()
print("sorted list: ")
print(*candyList, sep = ", ")

print(" ")
candyList.reverse()
print("reversed list: ")
print(*candyList, sep = ", ")

print(" ")
subList = []
for i in range (3): 
    sadTreat = input("Trick or treat?")
    subList.append(sadTreat)

print(" ")
candyList.append(subList)
print("candy list with sublist: ")
print(candyList)