from enum import Enum


class Choose(Enum):
    ADD = 1
    EDIT_REMOVE_SEARCH_VIEW = 2
    EXIT = 0


class SubChoose(Enum):
    EDIT = 'e'
    DELETE = 'd'
    SEARCH = 's'
    VIEW = 'v'
    RETURN = 'b'


contacts = []
while True:
    print(
        '1.Add Contact\n'
        '2.Edit/Remove/Search/View\n'
        '0.Exit\n'
    )
    choose = input()
    choose = int(choose)
    if choose == Choose.ADD.value:
        contacts.append(
            {
                'Name': input('Name='),
                'Number': input('Phone_Number='),
                'Address': input('Address=') 
            }
        )

    elif choose == Choose.EDIT_REMOVE_SEARCH_VIEW.value:
        print(
            'e.Edit\n'
            'd.Delete\n'
            's.Search\n'
            'v.View\n'
            'b.Return to Menu\n'
        )
        sub_choose = input()
        if sub_choose == SubChoose.DELETE.value:
            delete = input('Which Name you want to delete?=')
            for contact in contacts:
                if contact['Name'] == delete:
                    contacts.remove(contact)

        elif sub_choose == SubChoose.EDIT.value:
            edit = input('Enter Name to Edit:')
            for contact in contacts:
                if contact['Name'] == edit:
                    contact['Name'] = input('New Name=')
                    contact['Number'] = input('New Phone Number=')
                    contact['Address'] = input('New Address=')

        elif sub_choose == SubChoose.SEARCH.value:
            search = input('Enter Name to Search:')
            for contact in contacts:
                if contact['Name'] == search:
                    print('Here it is:')
                    print(f'Name: {contact["Name"]}')
                    print(f'Phone Number: {contact["Number"]}')
                    print(f'Address: {contact["Address"]}')
                else:
                    print('Not Found')

        elif sub_choose == SubChoose.VIEW.value:
            for contact in contacts:
                print(contact)

    elif choose == Choose.EXIT.value:
        break
