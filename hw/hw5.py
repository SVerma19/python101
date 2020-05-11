vaca_supplies = ["sunscreen", "swimsuit", "hat", "shades"]

stock = {
 "sunscreen": 3,
 "hat": 0,
 "swimsuit": 2,
 "shades": 15
}

prices = {
 "sunscreen": 4,
 "hat": 2,
 "swimsuit": 18.5,
 "shades": 11
}

#Q1
print("*********Q1*********")
total = 0
for i in vaca_supplies:
    total += prices[i] # can also use prices.get(i)
    print(total)
print("total amount of all prices in the list: ", total)
print("*********************")
print(" ")

#Q2
print("*********Q2*********")
totalList = []

for i in vaca_supplies:
    if (stock[i] > 0):
        totalList.append(prices[i])
print("list of items with stock prices > 0: ", totalList)
print("the total of items with stock prices > 0: ", sum(totalList))
print(" ")

for j in range(len(totalList)):
    totalList[j] -= 1
print("subtract one from item stock count list: ", totalList)
print("subtract one from item stock count total: ", sum(totalList))
print("*********************")