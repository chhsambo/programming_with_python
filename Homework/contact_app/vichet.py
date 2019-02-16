'''
Name: Vichet Pak
Type: Homework
Description: Contact list program, this program let user can create new, 
  search all,search by name only,delete 
'''
from enum import Enum


class Choice(Enum):
    ADD = 1
    SEARCH = 2
    DELETE = 3
    QUIT = 4


contacts = []
while True:
    print('\t\n                        Contact Menu ')
    print('\t                ************ ')
    print('                1. Add new contact')
    print('                2. Search contact')
    print('                3. Delete contact')
    print('                4. Quit')
    choice = input('\nPlease select your choice: ')
    choice = int(choice)
    if choice == Choice.ADD.value:
        print('>>>Add contact form:')
        cont_name = input('Name:')
        while not cont_name.strip():
            cont_name = input('Name:')
        cont_phone = input('Phone number:')
        while not cont_phone.strip():
            cont_phone = input('Phone number:')        
        contacts.append(
        {
          'name': cont_name,
          'phone': cont_phone
        })
        print('\n>>>Your contact has been added to contact list.')
            
    elif choice == Choice.SEARCH.value:     
        if len(contacts) == 0:
            print('\n>>>No record available!')
        else:
            print('>>>Search form:')
            print('\n1- View all contact')        
            print('2- View contact by name')
            view_choice = input('\nPlease select an option:')
            if view_choice == '1':
                print('All contact:')
                for view_cont in contacts:            
                    print(view_cont)
            elif view_choice == '2':
                search_name = input('Please put the name you want search: ')
                for search_cont in contacts:
                    if search_cont['name'].lower() == str(search_name).lower():
                        print('Contact:')
                        print(search_cont)              
                if not search_cont['name'].lower() == str(search_name).lower():
                    print('\n>>>Record not found!')
            else:
                print('\n>>>Invalid!')

    elif choice == Choice.DELETE.value:
        if len(contacts) == 0:
            print('\n>>>No record available!')
        else:
            del_cont = input('Please put contact name for delete:')
            for my_cont in contacts:
                if my_cont['name'].lower() == str(del_cont).lower():
                    contacts.remove(my_cont)
                    print('\n>>>Delete success!')
            if not my_cont['name'].lower() == str(del_cont).lower(): 
                print('\n>>>Record not found!')
                break

    elif choice == Choice.QUIT.value:
        break

    else:
      print('\n>>>Invalid!')
