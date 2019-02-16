'''
Name: Teng Chanto
Description: Assignment of the Contact list of the customers
'''
contacts = []
while True:
    print("Please select options:\n")
    print(
        "1. Add Contacts for Customers\n"
        "2. Edit/Remove/Search/DISPLAY\n"
        "0. Exit\n"
    )
    options = input()
    if options == "1":
        contact["Name"] = input("Name:")
        contact["Number"] = input("Phone_Number:")
        contact["Age"] = input("Age:")
        contact["Address"] = input("Address:")
        contacts.append(contact)

    elif options == "2":
        print(
            "E. Edit\n"
            "R. Remove\n"
            "S. Search\n"
            "D. Display\n"
            "b. Return to Menu\n"
        )
        suboptions = input()
        if suboptions == "E":
            edit_name = input("\n Enter Name to Edit Customers:")
            for contact in contacts:
                if contact["Name"] == edit_name:
                    contact["Name"] = input("New Name for customer is:")
                    contact["Number"] = input("New Phone for customer is:")
                    contact["Age"] = input("New age for the customer is:")
                    contact["Address"] = input("New Address for customer is:")

        elif suboptions == "R":
            remove_name = input("Which Name you want to remove?=")
            for contact in contacts:
                if contact["Name"] == remove_name:
                    contacts.remove(contact)
        
        elif suboptions == "S":
            search = input("Enter Name you want to Search:")
            for contact in contacts:
                if contact["Name"] == search:
                    print(f"Name: {contact['Name']}")
                    print(f"Phone Number: {contact['Number']}")
                    print(f"Age: {contact['age']}")
                    print(f"Address: {contact['Address']}")
                else:
                    print("Could not find name!")

        elif suboptions == "D":
            for contact in contacts:
                print(contact)

    elif options == "0":
        break
