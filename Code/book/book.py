import json

file_book = open('book.json', 'r')

book_data = json.load(file_book)
title = book_data['title']
author = book_data['author']

print(title)
print(author)