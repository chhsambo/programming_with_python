import json


def get_definition(search_word):
    with open("data.json") as data_file:
        data = data_file.read()
        data = json.loads(data)

        definition = data[search_word]
        return search_word, definition


search_word = input('Enter word: ')
search_word = search_word.lower()
word, definition = get_definition(search_word)
for d in definition:
    print(f'- {d}')