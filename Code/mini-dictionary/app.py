#import myutils
from myutils import get_definition, test_similar_word


while True:     # Exit when press \q
    search_word = input('\nEnter word: ')
    if search_word == '\\q':
        break

    # test_similar_word(search_word)
    
    definition = get_definition(search_word)
    for d in definition:
        print(f'- {d}')

    if not definition:
        print('Word not found!')