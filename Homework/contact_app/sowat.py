'''
Name: Kheang Sowat
Description: Create contact program
Functions: Add, Search, Edit and Delete
'''
from enum import Enum


class Choice(Enum):
    ADD = 1
    SEARCH_EDIT_DELETE = 2
    QUIT = 3


class Option(Enum):
    EDIT = 'E'
    DELETE = 'D'
    QUIT = 'Q'


my_contacts = [ ]

while True:
    print('\t\n -- -- -- -- -- -- Contact Menu -- -- -- -- -- -- --')
    print('|                                                   |')
    print('| 1. Add new contact________________________________|')
    print('| 2. Search, Edit or Delete_________________________|')
    print('| 3. Quit___________________________________________|')
    print('|                                                   |')
    print('-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n')
    print('-- -- -- -- -- -- This is my phone list -- -- -- -- |')
    print(f'\n{my_contacts} \n')

    choice = input('Please select your choice: ')
    choice = int(choice)
    if choice == Choice.ADD.value:
        name = input('\tName: ').title()
        while True:
            phone = input('\tTelephone: ')

            if phone.isdigit():
                phoneNumber = phone
                break
            else:
                print("\tTry again! That was not number")
                continue

        contact['name'] = f'{name}'
        contact['telephone'] = f'{phoneNumber}'
        my_contacts.append(contact)
        print('\tA new contact has been added!!!\n')    
    
    elif choice == Choice.SEARCH_EDIT_DELETE.value:
        while True:
            search = input('Enter a Name or a Phone Numer to search: ')
            for contact in my_contacts:
                if(
                    contact['name'].title() == search.title() or 
                    contact['telephone'] == search):
                    print(f'{contact["name"]} {contact["telephone"]}')
                    continue

            print('\nPress E to Edit or Press D to Delete or Q to Quit this option ')
            option = input('Please enter the option: ')

            if option == Option.EDIT.value:
                new_name = input("\tNew name: ").title()
                new_phone_number = input("\tNew telephone:")
                for contact in my_contacts:
                    if(
                        contact['name'].title() == search.title() or 
                        contact['telephone'] == search):
                        contact['name']= new_name
                        contact['telephone'] = new_phone_number
                        break
                break

            if option == Option.DELETE.value:
                for contact in my_contacts:
                    if contact['name'] == search.title() or contact['telephone'] == search:
                        my_contacts.remove(contact)
                        break
                break
            
            if option == Option.QUIT.value:
                break
     
    elif choice == Choice.QUIT.value:
        break
