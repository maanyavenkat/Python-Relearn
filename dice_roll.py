# Ask: roll the dice
# if user emters y
#   generate 2 random numbers between 1 and 6 and print them
#if user enters n
#   print "Thanks for playing!" and terminate --> therefore everything needs to be in an infintie loop
#else print "Invalid choice!" and ask again

import random

count = 0

while True: #for the input to show up again, need to have an infinite loop (ex: while loop)

    print()
    dice = input("Roll the dice? (y/n): ").lower()
    print()

    if dice == "y" :
        count += 1

        number = input("How many dice do you want to roll?: ") #specify how many dice to roll
        number = int(number)
        if number < 1:
            print("You must roll at least one die!")
            print()
            continue
        elif number >10:
            print("You can only roll up to 10 dice at a time!")
            print()
            continue
        else:
            for i in range(number):
                roll = random.randint(1,6)
                print(f"Die {i+1}: {roll}")

    elif dice == "n":
        print("Thanks for playing!")
        print(f"You rolled the dice {count} times!")
        print()
        break

    else:
        print("Invalid choice!")
        print()
  

