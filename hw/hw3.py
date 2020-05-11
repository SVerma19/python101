# A
list = [0, 1, 2, 3, 4]

# B
print("**********************************")
print("the second element in the list: ", list[1])
print("**********************************")
print(" ")

# C
print("**********************************")
list[3] = 20
print("the new list consists of: ", list)
print("**********************************")
print(" ")

# D
print("**********************************")
for i in range (len(list)):
    print(list[i])
print("**********************************")
print(" ")

# E
print("**********************************")
for i in list:
    if (i == 2):
        print(i)
print("**********************************")
print(" ")

# F
print("**********************************")
print("the length of the list is: ", len(list))
print("**********************************")
print(" ")

# G
print("**********************************")
list.append(26)
print(list)
print("**********************************")
print(" ")

# H
print("**********************************")
list.insert(2, 17)
print(list)
print("**********************************")
print(" ")

# I
print("**********************************")
newList = [65, 66, 67]
list.append(newList)
print(list)
print("**********************************")
print(" ")

# J
print("**********************************")
list.remove(list[5])
print("the new list consists of: ", list)
print("**********************************")
print(" ")

# K
print("**********************************")
list.pop(2)
print("the new list consists of: ", list)
print("**********************************")
print(" ")

# EXTRA CREDIT
print("**********************************")
bonusList = [90, 91, 92, 93, 94]
ogList = [0, 1, 2, 3, 4]

print(bonusList)
print(ogList)
print(" ")

bonusList.sort()
ogList.sort()
print("sorted list: ", bonusList)
print("sorted list: ", ogList)
print(" ")

bonusList.reverse()
ogList.reverse()
print("reversed list: ", bonusList)
print("reversed list: ", ogList)
print(" ")

bonusList.clear()
ogList.clear()
print("cleared bonusList: ", bonusList)
print("cleared ogList: ", ogList)
print("**********************************")