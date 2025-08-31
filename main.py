# imports
import sys
from stats import (
    get_book_text,
    get_word_count,
    get_characters_count,
    get_sorted_list
)


def print_results(b_path, w_count, c_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {b_path}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    for c in c_list:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")



# main operations
def main():
    if 1 == len(sys.argv):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    characters_count = get_characters_count(book_text)
    sorted_list = get_sorted_list(characters_count)
    print_results(book_path, word_count, sorted_list)


main()
