from art_book import logo, vs
from data_book import data
import random

print(logo)


def format_data(account):
    account_name = account["name"]
    account_dir = account["directions"]
    account_country = account["country"]
    return f"{account_name} publishes {account_dir}, from {account_country}"


def check_answer(guess, a_number_publications, b_number_publications):
    if a_number_publications > b_number_publications:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more number of publications? Type 'A' or 'B': ").lower()

    a_number_publications_count = account_a["number_publications"]
    b_number_publications_count = account_b["number_publications"]
    is_correct = check_answer(
        guess, a_number_publications_count, b_number_publications_count
    )

    if is_correct:
        score += 1
        print(f"You're right! Score {score}")
    else:
        game_should_continue = False
        print(f"You're wrong! Score {score}")
