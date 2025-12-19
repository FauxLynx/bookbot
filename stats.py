def book_word_count(book_text):
    counter = 0
    for i in book_text.split():
        counter += 1
    return counter

def character_count(book_text):
    book_text_lower = book_text.lower()
    character_count = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for letter in book_text_lower:
        if letter in character_count:
            character_count[letter] += 1
    return character_count

def sorter_helper(dictionary_to_sort):
    ready_to_sort = []
    for key in dictionary_to_sort:
        ready_to_sort.append({'letter': key, 'num': dictionary_to_sort[key]})
    return ready_to_sort

def sort_key(items):
    return items['num']

def sorted_dictionary(character_dict):
    sorted = sorter_helper(character_dict)
    sorted.sort(reverse=True, key=sort_key)
    return sorted




