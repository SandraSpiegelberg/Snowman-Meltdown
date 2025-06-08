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
    list_secret_letters = list(set(secret_word))
    list_secret_letters.sort()
    win = False

    print("Welcome to Snowman Meltdown!")
    while mistakes < 3 and win == False:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1
            if mistakes == 3:
                print("You lose! The secret word was:", secret_word)
        else:
            for letter in guessed_letters:
                if letter not in list_secret_letters:
                    guessed_letters.remove(letter)
            guessed_letters.sort()
            if guessed_letters == list_secret_letters:
                print('Congratulations, you saved the snowman!')
                win = True



if __name__ == "__main__":
    play_game()