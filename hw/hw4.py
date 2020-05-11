import random
from random import shuffle

# Q1
Beaches = ["Beaches"]
innerBeach = ["Naragansett Beach", "Pacific Ocean", "Salt Water", "Medium Waves"]
twoD = [Beaches, innerBeach]

print(twoD)
print("**********************")

print(twoD[1][0])
print(twoD[1][3])
print("**********************")

for i in twoD:
    for j in twoD:
        print(j, end = " | ")

print(" ")
print("**********************")


# Q2
randoms = []
for i in range (5):
    randoms.append(random.randint(1, 101))
print("array of random numbers: ", randoms)
print("**********************")

print("the minimum number in the list is: ", min(randoms))
print("**********************")

print("the maximum number in the list is: ", max(randoms))
print("**********************")

print("suffled list: ", shuffle(randoms))
print("**********************")

print(" ")
print("**********************")


# Q3
breakfast = ["eggs", "pancakes", "sausage", "bacon", "toast"]

breakfastTwo = breakfast.copy()

print("breakfast list one: ", breakfast)
print("**********************")
print("breakfast list two: ", breakfastTwo)
print("**********************")

print(" ")
print("**********************")


# Q4
desserts = ["cake", "cake pops", "pie", "brownies", "cookies"]
print("the original dessert list: ", desserts)
print("**********************")

desserts[1] = "ice cream"
desserts[3] = "cheesecake"

print("the new dessert list: ", desserts)
print("**********************")

print(" ")
print("**********************")


# Q5
softDrinks = ["fanta", "sprite", "coke", "pepsi", "dr. pepper"]
print("the original dessert list: ", desserts)
print("**********************")

desserts[0] = "gatorade"
desserts[4] = "powerade"

print("the new dessert list: ", desserts)
print("**********************")