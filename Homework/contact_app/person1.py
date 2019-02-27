person1 = {
    'name': 'Sopheak',
    'telephones': ['012345897', '012546978', '018768908'],
    'emails': ['sopheak1@gmail.com', 'sopheak2000@yahoo.com']
}

name = person1['name']
telephones = person1['telephones']
emails = person1['emails']

for tel in telephones:
    if tel.startswith('012'):
        print('Mobitel: ')
        print(tel)
