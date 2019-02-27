classmate = {
    'sopheak': {
        'id': 2389,
        'telephone': '012923989',
        'studies': ['c', 'c++ oop', 'c#']
    },
    'tola': {
        'id': 2390,
        'telephone': '012879953',
        'studies': ['html', 'css', 'php']
    }
}

print('-'*47)
for name, info in classmate.items():
    telephone = info['telephone']
    display_name = name.title()
    print(f'| {display_name.ljust(20)} | {telephone.ljust(20)} |')
    print('-'*47)

course = input("Enter course: ")
course = course.lower()
print('-'*67)
for name, info in classmate.items():
    display_name = name.title()
    studies = info['studies']
    if course in studies:
        display_studies = ', '.join(studies)
        display_studies = display_studies.upper()
        print(f'| {display_name.ljust(20)} | {display_studies.ljust(40)} |')
        print('-'*67)