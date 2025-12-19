from stats import book_word_count, character_count, sorted_dictionary
import sys


def get_book_text(x):
  with open(x) as f:
    book_text = f.read()
    return book_text

def main():
    if len(sys.argv) !=2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print('============ BOOKBOT ============')
    print('Analyzing book found at')
    print('----------- Word Count ----------')
    print(f'Found {book_word_count(book_text)} total words')
    print('--------- Character Count -------')
    character_count_dict = character_count(book_text)
    sorted = sorted_dictionary(character_count_dict)
    for i in sorted:
        letter = i['letter']
        num = i['num']
        print(f'{letter}: {num}')
    
main()
