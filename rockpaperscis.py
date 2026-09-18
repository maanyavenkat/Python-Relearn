#User input for Rock, Paper, or Scissors
#computer chooses a random choice
#if user wins, print "You win!"
#if computer wins, print "Computer wins!"
#keep count of wins for user and computer

#DRY = don't repeat yourself (use constants and a tuple to avoid repeating code)
 

import random

count_human = 0
count_computer = 0
count_tie = 0


ROCK = "r" #DRY - constants = variables that don't change, so we use all caps to indicate that
SCISSORS = "s" #DRY -  one place for r, s, and p so we can change them in one place if we want to change the letters
PAPER = "p"

emojis = {ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"} #dictionary {} bc we want to map the letters to emojis
choices = tuple(emojis.keys()) # DRY - change ("r", "p", "s") to tuple(emojis.keys()) to ensure no repetition of code


def get_user_choice(): #modularizing the code = adding methods to structure the code better
    while True:

        rps = input("Rock, Paper, or Scissors (r/p/s)? ").lower()
        if rps in choices:
            return rps
           
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")
        
def display_choices(rps, computer):
    print(f"You chose {emojis[rps]}")
    print(f"Computer chose {emojis[computer]}")

def determine_winner(rps, computer):
    if rps == computer:
        
        print("It's a tie!")
        print()
        count_tie += 1

    elif (
        (rps == ROCK and computer == SCISSORS) or 
        (rps == PAPER and computer == ROCK) or 
        (rps == SCISSORS and computer == PAPER)):
            print(f"You chose {emojis[rps]}")
            print(f"Computer chose {emojis[computer]}")
            print("You win!")
            print()

            count_human += 1

        
    else:
        print(f"You chose {emojis[rps]}")
        print(f"Computer chose {emojis[computer]}")
        print("You lose")
        print()
        count_computer += 1

def play_game():

    while True:
        rps = get_user_choice()

        computer = random.choice(choices) #computer chooses a random choice

        display_choices(rps, computer)

        determine_winner(rps, computer)

        keep_playing = input("Continue playing (y/n)? ").lower()

        if keep_playing == 'y':
            continue
        elif keep_playing == 'n':
            print(f"You won {count_human} times.")
            print(f"Computer won {count_computer} times.")
            print(f"There were {count_tie} ties.")
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            
            
play_game()


