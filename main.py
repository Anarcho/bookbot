def main():
    path = 'books/frankenstein.txt'
    print_report(path)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    dict_of_char = {}
    for i in text:
        if i in dict_of_char:
            dict_of_char[i] = dict_of_char[i] + 1
        else:
            dict_of_char[i] = 1
    return dict_of_char

def convert_to_alpha_list(dict):
    alpha_list = []
    for key in dict:
        char_dict = {}
        if key.isalpha() == True:
            char_dict["character"] = key
            char_dict["num"] = dict[key]
            alpha_list.append(char_dict)
    return alpha_list 

def sort_on(dict):
    return dict["num"]

def print_report(path):
    book_text = get_book_text(path)
    print(f'--- Begin report of {path} ---')

    words_count = get_word_count(book_text) 
    char_count = get_char_counts(book_text.lower())

    print(f'There are {words_count} words in book at path: {path} \n')

    alpha_list = convert_to_alpha_list(char_count)
    alpha_list.sort(reverse=True, key=sort_on)

    for i in alpha_list:
        print(f"The '{i['character']}' character was found {i['num']}")

    print('--- end report ---')
main()