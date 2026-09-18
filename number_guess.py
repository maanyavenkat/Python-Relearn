#guess the random number between 1 and 100
#if too high, tell user too high
#if too low, tell user too low
#once number is guessed, congratulate user and tell them how many tries it took

import random

count = 0
number = random.randint(1,100)

while True:
    print()
    guess = input("Guess the number between 1 and 100: ")
    count +=1

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")

    elif guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print(f"Congratulations! You guessed the number in {count} tries!")
        print()

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            count = 0
            number = random.randint(1,100)
        else:
            print("Thanks for playing!")
            print()
            break

