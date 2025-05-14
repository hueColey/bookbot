import sys 
    
from stats import get_num_words
from stats import letters_used
from stats import chars_dict_to_sorted_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    path = sys.argv[1] 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book_text = get_num_words(path)
    words = book_text.split()
    num_words = len(words)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    char_counts = letters_used(path)

    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")

    print("============= END ===============")


main()
