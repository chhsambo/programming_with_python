import json
import os

print("Welcome to Book Reader App!")
file_book_to_read = None

with open("book_db/books_list.json", "r") as book_files:
    books_data = json.loads(book_files.read())
    books = books_data["books"]
    
    for book in books:
        no = book["no"]
        print(f'\t{no}. {book["title"]}')

    choose_book = input("Choose book read: ")
    for book in books:
        if str(book["no"]) == choose_book:
            file_book_to_read = book["file"]

if file_book_to_read is not None:
    with open(f"book_db/{file_book_to_read}") as book_file:
        book = json.loads(book_file.read())
        os.system("cls")
        print("\t\t\t\t", book["title"])
        print(f"Author: {book['author']}")
        print(f"Release: {book['release']}")
        print(book["abstract"])
        print(book["chapters"])

print("\n\n\n\n")
input("\t\t\t\tNext Page (Press N) Previous Page (Press P)")
