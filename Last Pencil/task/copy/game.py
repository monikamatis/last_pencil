# importing necessary modules
import random

# setting the number of pencils in play

print('How many pencils would you like to use:')
number = input()

# checking input to make sure is numeric
# checking input to make sure number of pencils is not zero

while True:

    if number.isnumeric() is False:
        print("The number of pencils should be numeric")
        number = input()

    elif number == "0":
        print("The number of pencils should be positive")
        number = input()

    else:
        break

number = int(number)

# setting who plays first
# setting names of the players
# second player Jack is the bot

Name1 = "John"
Name2 = "Jack"

print('Who will be first (' + Name1 + ',' + Name2 + '):')

# checking if name is correct

while True:
    name = str(input())
    if name == Name1 or name == Name2:
        break
    else:
        print("Choose between", Name1, "and", Name2)

# play is here - printing the pencils and name of first player
# then asking for number of pencils to take - take_pencils
# number is decreased by this value and the name of the player is changed
# so on the next iteration the other player is called
# play stops when number of pencils reaches (or goes below) 0

while number > 0:
    print('|' * int(number))
    print(name + "'s turn!")

# find out if the bot (Name2 = Jack) is playing
# and setting moves for the bot with winning strategy and randomised moves if there is no clear winning position

    if name == Name2:

        if number in range(2, 1000000, 4):
            take_pencils = 1
            print(take_pencils)

        elif number in range(3, 1000001, 4):
            take_pencils = 2
            print(take_pencils)

        elif number in range(4, 1000002, 4):
            take_pencils = 3
            print(take_pencils)
        #     elif 1 < number < 5:
        #         take_pencils = number - 1
        #         print(take_pencils)

        else:

            # checking if random number doesn't go against the rule

            while True:
                take_pencils = random.randint(1, 3)
                if take_pencils > number:
                    continue
                else:
                    break
            print(take_pencils)

    else:
        take_pencils = input()

# setting limit for one player
# and checking, if not too many

    while True:

        # skipping checks for Jack as the bot plays only according to rules

        if name == Name2:
            break

        elif take_pencils.isnumeric() is False:
            print("Possible values: '1', '2' or '3'")
            take_pencils = input()
            continue

        elif int(take_pencils) > 3 or int(take_pencils) < 1:
            print("Possible values: '1', '2' or '3'")
            take_pencils = input()
            continue

        elif number - int(take_pencils) < 0:
            print("Too many pencils were taken")
            take_pencils = input()
            continue

        else:
            break

    number -= int(take_pencils)

    if name == Name1:
        name = Name2
    else:
        name = Name1

print(name, "won!")
