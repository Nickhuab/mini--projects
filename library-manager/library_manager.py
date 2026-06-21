books=[]
def load_book():
    try:
        with open('book.txt','r') as f :
            for line in f:
               title,name,copies=line.strip().split(',')
    
               books.append({
                    'title':title,
                    'Author':name,
                    'copies':int(copies)
                })

    except FileNotFoundError:
        pass
load_book()

def save_book():
    with open('book.txt','w') as f:
        for items in books:
            f.write(f"{items['title']},{items['Author']},{items['copies']}\n")

def add_book():
    try:
        title=input('Enter name of book :')
        name=input("Enter author's name :")
        copies=int(input('enter no. of copies :'))
        for item in books:
            if title==item['title']:
                item['copies']+=copies
                print('added successfully')
                break
        else:
            books.append({'title':title,'Author':name,'copies':copies})
            print('Book added successfully')
        save_book()
    except ValueError:
        print('invalid input')

def view_book():
    if not books:
        print('No books available')
        return
    
    for i,items in enumerate(books,start=1):
        print(f"{i}.Title: {items['title']}\nAuthor: {items['Author']}\nAvailable copies: {items['copies']}\n")

def borrow_book():
    try:
        borrow=input('enter name of to borrow :')
        number=int(input(f'enter no. of copies to borrow :'))
        for book in books:
            if borrow==book['title']:
                book['copies']-=number
                print(f'{borrow} borrowed,{number} copies')
                break

        else:
            print(f"{borrow} is not available")
        save_book()

    except ValueError:
        print('Invalid input!!')

def search_book():
    try:
        name=input('enter name of book to search :')
        for book in books:
            if name==book['title']:
                print(f"Title:{book['title']}\nAuthor:{book['Author']}\nAvailable copies:{book['copies']}")  
                break
        else:
            print(f'{name} is not available')
        save_book()

    except ValueError:
        print('Invalid input!')

def return_book():
    try:
        book_name=input('enter name of book to return :')
        bok=int(input('enter no. of books to return :'))
        for item in books:
            if book_name==item['title']:
                item['copies']+=bok
                break
        else:
            user=input('enter name of author :')
            books.append({'title':book_name,
                      'Author':user,
                      'copies':bok
                      })
        print('book returned successfully')
        save_book()
    except ValueError:
        print('Invalid input!')

def delete_book():
    view_book()
    try:
        user=int(input('enter position of book to delete :'))
        if user<1 and user>len(books):
            print('Invalid input,enter valid position of book')

        else:
            books.pop(user-1)
            print('book deleted successfullly')
        save_book()

    except ValueError:
        print('Invalid input')

while True:

    print('\n1.Add book\n2.view books\n3.Borrow books\n4.Search books\n5.Return books\n6.delete books\n7.Exit')
    user=input('\nenter your choice :')

    if user=='1':
        add_book()

    elif user=='2':
        view_book()

    elif user=='3':
        borrow_book()

    elif user=='4':
        search_book()

    elif user=='5':
        return_book()

    elif user=='6':
        delete_book()

    elif user=='7':
        break
    else:
        print('Invalid input!')
