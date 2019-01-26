import os

path = 'text.txt'

if os.path.isfile(path):
    print(f"File {path} is found!")

text = open(path).read()

# print(text)