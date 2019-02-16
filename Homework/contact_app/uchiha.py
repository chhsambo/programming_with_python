from enum import Enum


class Menu(Enum):
    SHOW_CONTACT = 1
    MANAGE_CONTACT = 2
    SEARCH_CONTACT = 3
    EXIT = 0


class ManageMenu(Enum):
    ADD = 1
    DELETE = 2
    EDIT = 3
    BACK = 0


contacts = {
    'Sokha': '012830551',
    'Linda': '081678567',
    'Nika': '0963823824',
    'Nita': '0109878768',
}


def not_found():
    print('Not found')


def edit():
    while True:
        print(contacts)
        print('1. Edit')
        print('0. Exit')
        edit_menu = input('>>>')
        if edit_menu == '1':
            print(contacts)
            edit_name = input('Input name you what to edit:')#Name
            is_find = False
            for name in contacts.keys():
                if edit_name.title() == name.title():
                    is_find = True
                    break

            if is_find:
                while True:
                    print('1. Edit name')
                    print('2. Edit PhoneNumber')
                    print('0. Exit')
                    Menu=input('>>>')
                    if Menu == '1':
                        new_name = input('Input new name:')
                        contacts[new_name] = contacts[name]
                        del contacts[name]
                    elif Menu == '2':
                        new_phone_number = input('Input new PhhoneNumber:')
                        contacts[name] = new_phone_number
                        print(contacts[name])
                    elif Menu == '0':
                        break
            else:
                not_found()
        elif edit_menu == '0':
            break
    return


def add():
    while True:
        print('1. Add New')
        print('0. Exit')
        add_menu = input('>>>')
        if add_menu == '1':
            new_name = input('Input new name:').title()#NewName 
            new_phone_number = input('Input new PhoneNumber:').title()#NewPhoneNumber
            contacts[new_name] = new_phone_number
            print(contacts)
        elif add_menu == '0':
            break
    return


def delete():
    while True:
        print(contacts)
        print('1. Delete')
        print('0. Exit')
        delete_menu = input('>>>')
        if delete_menu == '1':
            print(contacts)
            input_name = input('Input Name u want to delete:')
            print('Press 0 for exit')
            is_find = False
            for name in contacts.keys():
                if input_name.title() == name.title() :
                    is_find = True
                    break 
            if is_find:
                del contacts[input_name.title()]
                print(contacts)
            else:
                not_found()
        elif delete_menu == '0':
            break
    return


def manage():
    while True:
        print('1. Add new')
        print('2. Delete')
        print('3. Edit your contact')
        print('0. Go Back')
        manage_menu = input('>>>')
        manage_menu = int(manage_menu)
        if manage_menu == ManageMenu.ADD.value:
            add()
        elif manage_menu == ManageMenu.DELETE.value:
            delete()
        elif manage_menu == ManageMenu.EDIT.value:
            edit()
        elif manage_menu == ManageMenu.BACK.value:
            break
    return


def search():
    s = input('Input name you want to search:')
    is_find = False
    for name in contacts.keys():
        if s.title() == name.title():
            is_find = True
            break

    if is_find:
        print(f'{name.title()} and {contacts[name]}')
    else:
        not_found()
    return


print('Welcome to my contact project')   
while True:    
    print('1. Show the contact')
    print('2. Manage your contact')
    print('3. Search')
    print('0. Exit')
    menu = input('>>>') 
    menu = int(menu)
    if menu == Menu.SHOW_CONTACT.value:
        print(contacts)
    elif menu == Menu.MANAGE_CONTACT.value:
        manage()
    elif menu == Menu.SEARCH_CONTACT.value:
        search()
    elif menu == Menu.EXIT.value:
       break
