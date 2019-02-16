from enum import Enum

class Command:
    READ = 'R'
    CREATE = 'C'
    SEARCH = 'S'
    EDIT = 'E'

def create_contact():
    print("Contact created!")
    print(
        f'{Command.READ}'
        f'{Command.CREATE}'
    )
    
command = input("Enter what you want to do: ")
if command == Command.READ:
    print(Command.READ)
elif command == Command.CREATE:
    print(Command.CREATE)
else:
    print(command)
    create_contact()