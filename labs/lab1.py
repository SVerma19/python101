# Debug all errrors found in this program so that the output result is displayed correctly to the user 

import random

user = input("choose your weapon!")
comp = random.choice(['rock','paper','scissors'])

print('user (you) chose:', user)
print('comp (me) chose:',  comp)

if (user == 'rock' and comp == 'paper'):
    print('YOU LOSE!')
if (user == 'rock' and comp == 'scissors'):
    print('YOU WIN!')
if (user == 'rock' and comp == 'rock'):
    print('TIE')

if (user == 'paper' and comp == 'rock'):
    print('YOU LOSE!')
if (user == 'paper' and comp == 'rock'):
    print('YOU WIN!')
if (user == 'paper' and comp == 'paper'):
    print('TIE')

if (user == 'scissors' and comp == 'rock'):
    print('YOU LOOSE!')
if (user == 'scissors' and comp == 'paper'):
    print('YOU WIN!')
if (user == 'scissors' and comp == 'scissors'):
    print('TIE')


