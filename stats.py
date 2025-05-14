def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def letters_used(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        letter_count = {}
        for char in file_contents:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
        return letter_count



def sort_on(dict):
    return dict["num"]



def chars_dict_to_sorted_list(char_dict):
    char_list = []
    for char in char_dict:
        char_info = {"char": char, "num": char_dict[char]}
        char_list.append(char_info)
    char_list.sort(reverse=True, key=sort_on)
        
    return char_list

