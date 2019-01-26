import os

print("File Finder Program")
print("===================")

path = input("Location: Downloads (Default) ")
if path.strip() == "":
    path = "C:/Users/Sambo/Downloads"

find = input("What do you want to find? ")

for root, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(find):
            print(f"{root} -- {filename}")