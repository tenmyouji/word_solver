import csv
import string
from string import upper


def word_dict():  # generate the word dictionary
    with open('./src/english_words.txt', 'r') as imported_dict:
        reader = csv.reader(imported_dict)
        dictionary = {}
        for row in reader:
            if row[0].isalpha():
                if len(row[0]) not in dictionary:
                    dictionary[len(row[0])] = [upper(row[0])]
                else:
                    dictionary[len(row[0])].append(upper(row[0]))
        return dictionary


def five_letter_word_dict():  # generate the word dictionary
    with open('./src/5_letter_words.txt', 'r') as imported_dict:
        reader = csv.reader(imported_dict, delimiter=',', quotechar='"')
        dictionary = []
        for word in reader.next():
            if word not in dictionary:
                 dictionary.append(upper(word))
        return dictionary


def words(mode, length):  # generate a list of words with a length n
    if mode == 1:
        word_list = word_dict()
        return word_list[length]
    else:
        word_list = five_letter_word_dict()
        return word_list


def generate_letter_freq(words):
    frequencies = dict.fromkeys(string.ascii_uppercase, 0)
    for word in words:
        letters = []
        for letter in word:

            if letter not in letters:
                letters.append(letter)
                frequencies[letter] += 1
    return frequencies
