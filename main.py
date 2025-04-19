from stats import *
import sys

def get_book_text(filepath):
    file_content = ""

    with open(filepath) as f:
        file_content = f.read()

    return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    count_key = 0
    char_key = ""
    book = get_book_text(f"{sys.argv[1]}")
    num_words = count_words(book)
    original_dict = get_number_of_each_char(book)
    list_of_dicts = get_sorted_list_of_dict(original_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # for dict in list_of_dicts:
    #     for key in dict:
    #         if key == "character":
    #             char_key = dict[key]
    #         elif key == "count":
    #             count_key = dict[key]
    #     if char_key.isalpha() is True:    
    #         print(f"{char_key}: {count_key}")


    for dict in list_of_dicts:
        if dict['character'].isalpha():
            print(f"{dict['character']}: {dict['count']}")
    print("============= END ===============")


main()
