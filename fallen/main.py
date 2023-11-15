import random
from fallen_words import word_list
from fallen_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(f"Shh, that's a hint {chosen_word}.")
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You named {guess}, that's not in the word. You lose your balance")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You fell")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
