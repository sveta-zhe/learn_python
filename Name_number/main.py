from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

print(logo)


def number_check(player_choice, chosen_number, attempts):
    if player_choice > chosen_number:
        print("Need a lower number!")
        return attempts - 1
    elif player_choice < chosen_number:
        print("Need a higher number!")
        return attempts - 1
    else:
        print(f"You win! The number is: {chosen_number}")


def difficult_level():
    level = input("Choose a difficult level.Type 'h' hard or 'e' easy: ")
    if level == "e":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcom to the Number Game!")
    print(
        """The computer has chosen a number from 1 to 100.\n
    You have 5 attempts in the difficult level and 10 attempts in the easy one"""
    )
    chosen_number = randint(1, 100)
    attempts = difficult_level()

    player_choice = 0
    while player_choice != chosen_number:
        print(f"You have {attempts} attempts trying to guess the number")
        player_choice = int(input("Please select a number: "))
        attempts = number_check(player_choice, chosen_number, attempts)
        if attempts == 0:
            print("You've run out of attempts. You lose")
            return
        elif player_choice != chosen_number:
            print("Try to guess the number again!")


game()
