import random
import string
from string import upper
from termcolor import colored

import word_util
import word_ai
import main


def print_current_guess(current_guess):
    print("Try guessing: " + current_guess)


def get_best_guess():
    num_guesses = 0
    length = 5
    alphabet_guess = dict.fromkeys(string.ascii_uppercase, 0)
    previous_guesses = []
    current_guess = ""
    mode = 0

    while num_guesses < 6:
        if current_guess == "":
            current_guess = word_ai.make_guess(previous_guesses, alphabet_guess, mode, length)
            print_current_guess(current_guess)

        else:
            print ("Help Ms. AI figure out the word! \nC = correct position \nI = incorrect position \nX = not in word")
            word = upper(raw_input())
            previous_guesses.append([])
            for i, g in enumerate(word):
                if g == "C":
                    state = 3
                elif g == "I":
                    state = 2
                elif g == "X":
                    state = 1
                else:
                    main.print_input_error()
                previous_guesses[num_guesses - 1].append((current_guess[i], state))
                alphabet_guess[current_guess[i]] = state
            current_guess = word_ai.make_guess(previous_guesses, alphabet_guess, mode, length)
            print_current_guess(current_guess)

        num_guesses += 1
