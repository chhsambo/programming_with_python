'''
Name: Kim Solei
Type: Homework1
Keyword: List & Dictionary
Description: Contact list with functionalities: add, edit, search and remove
'''
import os
from enum import Enum


class Command(Enum):
    ADD = 1
    VIEW_EDIT_READ = 2
    EXIT = 0


class SubCommand(Enum):
    SEARCH = 's'
    REMOVE = 'r'
    EDIT = 'e'
    GO_TO_MENU = 'm'


contact_list = []
while True:
    os.system('cls')
    total_contacts = len(contact_list)
    print('.....Contact List.....')
    print('1. Add new contact')
    print(f'2. View/Edit/Remove({total_contacts})')
    print('0. Exit')
    print('......................')

    option = input('Select an option: ')
    option = int(option)
    if option == Command.EXIT.value:
        break

    elif option == Command.ADD.value:
        os.system('cls')
        contact['name'] = input('Name:')
        contact['phone_num'] = input('Phone:')
        contact['email'] = input('Email:')
        contact['address'] = input('Address:')
        contact_list.append(contact)
        print('One new contact added!')
        os.system('pause')

    elif option == Command.VIEW_EDIT_READ.value:
        while True:
            os.system('cls')
            header = (
                'No.'.ljust(10) +
                'Name'.ljust(25) +
                'Phone number'.ljust(25) +
                'Email'.ljust(30) +
                'Address'
            )
            underline = '.' * 98
            print(header)
            print(underline)
            no = 1
            for contact in contact_list:
                print(  
                    str(no).ljust(10) +
                    contact['name'].ljust(25) + 
                    contact['phone_num'].ljust(25)+ 
                    contact['email'].ljust(30) + 
                    contact['address']
                )
                no += 1
            print(underline)
            print('Input <s:Search, r:Remove, e:Edit, m:Go to menu>   :')
            suboption = input()
            if suboption.lower() == SubCommand.GO_TO_MENU.value:
                break

            elif suboption.lower() == SubCommand.SEARCH.value:
                search = input('Search for:')
                search = search.lower()
                os.system('cls')
                print(header)
                print(underline)
                for contact in contact_list:
                    if (
                        contact['name'].lower() == search or 
                        contact['phone_num'].lower() == search or 
                        contact['email'].lower() == search or 
                        contact['address'].lower() == search):
                        no = 1
                        print(  
                            str(no).ljust(10) +
                            contact['name'].ljust(25) + 
                            contact['phone_num'].ljust(25) + '\t' + 
                            contact['email'].ljust(30) + '\t' + 
                            contact['address']
                        )
                        no += 1
                print(underline)
                os.system('pause')

            elif suboption.lower() == SubCommand.REMOVE.value:
                search = input('Enter contact name to remove>>')
                deleted = False

                for contact in contact_list:
                    if contact['name'].lower() == search.lower():
                        contact_list.remove(contact)
                        deleted = True
                        break

                if not deleted:
                    print('No contact found!')
                else:
                    print(f'<{search}> removed.')  
                os.system('pause')

            elif suboption.lower() == SubCommand.EDIT.value:
                search = input('Enter name to edit>>')
                edited = False
                for contact in contact_list:
                    if contact['name'].lower() == search.lower():
                        contact['name'] = input('Name:')
                        contact['phone_num'] = input('Phone:')
                        contact['email'] = input('Email:')
                        contact['address'] = input('Address:')
                        edited = True
                        break

                if not edited:
                    print('No contact found!')
                else:
                    print(f'<{search}> edited.')   
                os.system('pause')
    else:
        print(option)
        os.system('pause')
