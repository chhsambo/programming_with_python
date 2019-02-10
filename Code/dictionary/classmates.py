classmates = {
    'sopheak': 'c',
    'tola': 'php',
    'chenda': 'c#',
    'nicolas': 'java',
    'sambo': 'python'
}
friends = ['chenda', 'nicolas']

for name in classmates.keys():
    print(name.title())

    if name in friends:
        print(
            f'  Hi {name.title()},'
            f'I see you know {classmates[name].upper()}'
        )