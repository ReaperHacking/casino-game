#In This Casino Game The Player bets an amount and guesses the number that the casino bot will roll!
#If The Player rolls correctly, they win the amount they bet and vice versa!
#If The Player loses all their money (0 or under) the game exits!

import random

# Intro
print("Welcome to my casino game! You will enter in a betting amount and if you guess the number correctly (1-6), you win!")
print("If you guess it incorrectly (1-6), you lose! You can keep playing until you run out of money!\n")

user_bet = int(input("Enter a betting amount: "))

while user_bet > 0:
    # Initializing Variables
    casino_bot = random.randint(1, 6)
    user_guess = int(input("Enter a guess between 1 and 6: "))

    if user_bet == 0:
        print("No more balance! :/")
        break

    # Initiating The Casino Conditions
    def casino_conditions(user_guess, casino_bot, user_bet):
        if user_guess == casino_bot:
            print(f"Congrats! You Won! The number was {casino_bot}! +{user_bet}")
            return user_bet
        elif user_guess < casino_bot or user_guess > casino_bot:
            print(f"Sorry! You lose! The number was {casino_bot}! -{user_bet}")
            return -user_bet
        else:
            print("That's not a number!")
            return 0

    bet_result = casino_conditions(user_guess, casino_bot, user_bet)

    user_bet += bet_result

    #Function for when user loses all balance
    if user_bet == 0:
        print("No more balance! :/")
        break

    #Asking user if they want to replay the game
    replay = input("Would you like to replay? (Y/N): ").upper()
    if replay == "N":
        break
    elif replay == "Y":
        continue
    else:
        print("Error! Not Y or N!")
        break





