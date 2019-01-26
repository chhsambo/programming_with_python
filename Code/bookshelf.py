print('My Favorite Books')

english_book = 'Book 1'

bookshelf = ['Zero to One',
             'Getting Real',
             'Fluent Python',
             english_book]
while True:
    print(bookshelf)
    print('\nSelect action to do!')
    print('(1) Add book')
    print('(0) Exit')
    choose = input('Choose: ')

    choose = int(choose)
    if choose == 0:
        break
    elif choose == 1:
        book_title = input('Enter your book title: ')
        bookshelf.append(book_title)        
    
    print('\n\n')

print('Thanks you for using my program.')








