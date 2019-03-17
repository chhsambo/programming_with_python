import utils


search_word = input('Enter word: ')
# search_word = search_word.lower()
definition = utils.get_definition(search_word)
for d in definition:
    print(f'- {d}')

if not definition:
    print('Word not found!')