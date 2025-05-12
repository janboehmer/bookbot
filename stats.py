import sys
from os.path import split
from turtledemo.paint import switchupdown


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    counter = 0
    words = file_contents.split()
    for word in words:
        counter += 1
    message = f"Found {counter} total words"
    return message

def get_num_letters(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    num_letters = {}

    words = file_contents.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            num_letters[letter] = 0

    for word in words:
        for letter in word:
            letter = letter.lower()
            num_letters[letter] += 1


    return num_letters

def get_sorted_dicts(dict_of_words, word_count, filepath):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"{word_count}")
    print("--------- Character Count -------")


    sorted_items = sorted(dict_of_words.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items:
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")

    return ""