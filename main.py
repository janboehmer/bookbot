from stats import get_num_words, get_num_letters, get_sorted_dicts
import sys


def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]

    dict_letters_num = get_num_letters(file)
    word_count = get_num_words(file)
    print(get_sorted_dicts(dict_letters_num, word_count, file))
main()