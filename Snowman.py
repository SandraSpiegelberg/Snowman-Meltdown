'''
Game code for Snowman-Meltdown

'''

import random

#Snowman ASCII Art stages
from art_stages import STAGES

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

    display_game_state(mistakes, secret_word, guessed_letters)

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)
    guessed_letters.append(guess)



if __name__ == "__main__":
    play_game()