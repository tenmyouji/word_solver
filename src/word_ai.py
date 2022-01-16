import random
import word_util


def remove_word(alphabet_guess, word):
    for l in word:
        if alphabet_guess[l] == 1:  # removes if not in word at all
            return False
    for l in alphabet_guess.keys():
        if alphabet_guess[l] == 2 and l not in word:
            return False
    return True


def remove_incorrect_position(previous_guesses, word):
    for i, letter in enumerate(word):
        for guess in previous_guesses:
            if letter == guess[i][0] and guess[i][1] == 2:  # removes word is in incorrect position
                return False
            elif letter != guess[i][0] and guess[i][1] == 3:  # removes word if position is already occupied
                return False
    return True


def most_frequent(potential_words, frequencies):
    best_guess = ('', 0)
    for word in potential_words:
        word_sum = 0
        letters = []
        for letter in word:
            if letter not in letters:
                word_sum += frequencies[letter]
                letters.append(letter)
                if word_sum > best_guess[1]:
                    best_guess = (word, word_sum)
    return best_guess


def make_guess(previous_guesses, alphabet_guess, mode, length):
    potential_words = set(word_util.words(mode, length)).copy()

    filtered_alphabet = filter(lambda word: remove_word(alphabet_guess, word), potential_words)
    filtered_positions = filter(lambda word: remove_incorrect_position(previous_guesses, word), filtered_alphabet)
    frequencies = word_util.generate_letter_freq(potential_words)
    guess = most_frequent(filtered_positions, frequencies)
    return guess[0]


def filter_amanda(predicate, list):
    # returns copy of list with all items deemed false removed
    list_filtered = []
    for item in list:
        if predicate(item):
            list_filtered.append(item)
    return list_filtered


def filter_rec(predicate, list):
    # returns copy of list with all items deemed false removed
    if len(list) == 0:
        return []
    elif predicate(list[0]):
        return [list[0]] + filter_rec(predicate, list[1:])
    else:
        filter_rec(predicate, list[1:])
