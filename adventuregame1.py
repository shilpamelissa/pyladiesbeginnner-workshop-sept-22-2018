#Task 1
"""
print()
print('welcome to the dungeon!')
print('do you go want to go through door 1 or door 2?')

door = input('>')

if door == '1':
    print('there is a nice vampire asking you if you enjoy life.')
    print('what do you do?')
    print('1. smile and nod')
    print('2. scream and run')

    vampire = input('>')

    if vampire == '1':
        print('congratulations, you found a new friend')
    elif vampire == '2':
        print('sorry, the vampire is faster. You are now dinner.')
    else:
        print('you are not that good with numbers, are you?')

    #Exercise C

else:
    print('you are not that good with numbers, are you?')
"""

print()

name = input('What is your first name?')
place = input('Where do you live?')

print(f'welcome to the dungeon, {name} from {place}')

print('do you want to go through door 1 or door 2?')

def genderverify(gender):
    if gender == 'male':
        print('hey bro')
    elif gender == 'female':
        print('hey girl')
    else:
        print('gender not recognized')

genderverify(gender)

print('What is your gender?')

gender = input('>')

door = input('>')

def dungeon():
    print('you are not so good with numbers, are you?')

if door == '1':
    print('there is a nice vampire asking if you enjoy life')
    print('what do you do?')
    print('1. smile and nod')
    print('2. scream and run')

    vampire = input('>')

    if vampire == '1':
        print(f'congratulations {name}, you made a new friend!')
    elif vampire == '2':
        print (f'sorry, {name}! The vampire is faster and you are now dinner!')
    else:
        dungeon()

elif door == '2':


else:
    dungeon()



