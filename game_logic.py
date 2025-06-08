'''
Game code for Snowman-Meltdown

'''

import random

#Snowman ASCII Art stages
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    #print the Stages of the snowman
    print(STAGES[mistakes])
    display_word = ''
    #display of the secret word
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print('Word:', display_word, ' \n')



def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # TODO: Build your game loop here.
    while mistakes <= 3 or len(guessed_letters) >= len(secret_word): #ist noch nicht richtig der zweite Teil
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1




if __name__ == "__main__":
    play_game()