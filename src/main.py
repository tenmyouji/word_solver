import random
import string
from string import upper
from termcolor import colored

import word_util
import word_ai
import wordle_guesser


# printing functions
def print_alphabet(alphabet):
    output = ""
    for key in string.ascii_uppercase:
        if alphabet[key] == 0:
            output = output + key
        if alphabet[key] == 1:
            output = output + colored(key, "grey")
        if alphabet[key] == 2:
            output = output + colored(key, "yellow")
        if alphabet[key] == 3:
            output = output + colored(key, "green")
        output = output + ' '
    print(output)


def print_remaining_guesses(n):
    print("Remaining guesses: {0}".format(6 - n))


def print_input_error():
    print("Please input a valid response.")


def print_incorrect_guess(n):
    print("Your guess must be " + str(n) + " letters long!")


def print_invalid_word(word):
    print(upper(word) + " is not a valid word!")


def print_finished_game(win, secret):
    if win:
        print("You lose :( The word was " + upper(secret) + ".")
    else:
        print("You win :)")


def print_guess(resp):
    print(resp)


# helper functions
def change_colour(colour, letter):
    return colored(upper(letter), colour)


def finished_game(guess, secret):
    if guess != secret:
        return True


def replay_game():
    while True:
        play_again = raw_input("Play again? (y/n): ")
        if play_again == "n":
            exit()
        elif play_again == "y":
            start_game()
        else:
            print_input_error()


# main game functions
def start_game():  # start game, choose mode
    print("0: Wordle Guesser AI, 1: Play")
    mode = input("Choose mode: ")
    if mode == 1:
        while True:
            word_length = input("Choose word length: ")
            if not word_length.isnumeric():
                word_list = word_util.words(mode, word_length)
                if len(word_list) != 0:
                    secret = random.choice(word_list)
                    word_set = set(word_list)
                    play_game(secret, word_set)
                else:
                    print_input_error()
            else:
                print_input_error()
    else:
        wordle_guesser.get_best_guess()


def play_game(secret, word_set):  # play the game
    current_guess = ""
    num_guesses = 0
    alphabet_guess = dict.fromkeys(string.ascii_uppercase, 0)
    previous_guesses = []  # make a list with previous guesses (tuples, letter and state)

    while current_guess != secret and num_guesses < 6:
        print_alphabet(alphabet_guess)
        print_remaining_guesses(num_guesses)
        current_guess = upper(raw_input("Make your guess: "))
        if current_guess == "":
            current_guess = word_ai.make_guess(previous_guesses, alphabet_guess, len(secret))
        resp = range(len(secret))

        if len(current_guess) != len(secret) or not current_guess.isalpha():
            print_incorrect_guess(len(secret))
        elif current_guess not in word_set:
            print_invalid_word(current_guess)
        else:
            previous_guesses.append([])
            for l in range(len(secret)):
                letter = current_guess[l]
                if letter == secret[l]:
                    state = 3
                    resp[l] = change_colour("green", letter)
                else:
                    if letter in secret:
                        state = 2
                        resp[l] = change_colour("yellow", letter)
                    else:
                        resp[l] = change_colour("red", letter)
                        state = 1

                previous_guesses[num_guesses].append((letter, state))
                alphabet_guess[letter] = state

            resp_str = ("".join(str(i) for i in resp))
            num_guesses += 1
            print_guess(resp_str)

    print_finished_game(finished_game(current_guess, secret), secret)
    replay_game()


# start playing!
if __name__ == "__main__":
    start_game()
