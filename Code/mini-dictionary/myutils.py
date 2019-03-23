import json
from difflib import get_close_matches


def get_definition(search_word):
    with open("data.json") as data_file:
        data = data_file.read()
        data = json.loads(data)

        definition = []
        if search_word.lower() in data.keys():
            definition = data[search_word.lower()]
        elif search_word.title() in data.keys():
            definition = data[search_word.title()]
        elif search_word.upper() in data.keys():
            definition = data[search_word.upper()]

        # NEW CODE
        if not definition:
            similar_words = get_close_matches(
                search_word, 
                data.keys(),
                n=3,
                cutoff=0.8
            )
            if similar_words:
                search_similar = input(f'Do you mean {similar_words[0]} (Y/n)?')
                if search_similar.lower() == 'y':
                    definition = data[similar_words[0]]
        
        return definition


def test_similar_word(search_word):
    with open("data.json") as data_file:
        data = data_file.read()
        data = json.loads(data)

        similar_words = get_close_matches(search_word, data.keys(),
            n=3, 
            cutoff=0.8
        )
        print(similar_words)

