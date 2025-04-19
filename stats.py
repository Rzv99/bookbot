def count_words(string):
    counter = 0
    words = string.split()
    for word in words:
        counter += 1
    return counter 


def get_number_of_each_char(string):
    lowered_string = string.lower()
    set_with_all_chars_in_string = set()
    my_dict = {}

    for char in lowered_string:
        set_with_all_chars_in_string.add(char)

    for char in set_with_all_chars_in_string:
        my_dict[char] = 0

    for char in lowered_string:
        if char in set_with_all_chars_in_string:
            my_dict[char] += 1

    return my_dict

def sort_on(dict):
    return dict["count"]

def get_sorted_list_of_dict(dict):
    my_list = []

    for key in dict:
        my_dict = {
            "character": key,
            "count": dict[key]
        }
        my_list.append(my_dict)

    my_list.sort(reverse=True, key=sort_on)
    
    return my_list