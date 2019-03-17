import json


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
        return definition


def welcome():
    print('Welcome to Mini Dictionary')