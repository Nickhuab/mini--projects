
d={}

def valid_marks():
    try:
        marks=int(input('enter marks :'))
        return marks
    except ValueError:
        print('invalid number')

def view_student():
     for name,marks in d.items():
                print(f'Name:{name} | Marks:{marks}')


def search_student():
    name=input('enter name :')
    if name in d:
        print(f'Name:{name} | Marks:{d[name]}')
    else:
        print('name not found')

def load_students():
    try:
        with open('student.txt','r') as f:
            for line in f:
                name,marks=line.strip().split(':')
                d[name]=int(marks)
    except FileNotFoundError:
        print('file doesnt exist')
load_students()

def add_student():
    try:
        name=input('enter name of student :')
        if name not in d:
            marks=valid_marks()
            d[name]=marks
        else:
            print('student already exists')
        save_student()
    except ValueError:
        print('enter valid number')

def delete_student():
    name=input('enter name :')
    if name in d:
        d.pop(name)
        print('student deleted')
    else:
        print('name doesnt exist')
    save_student()

def update_marks():
    try:
        name=input('enter name :')
        if name in d:
            marks=int(input('enter marks :'))
            d[name]=marks
            save_student()
        else:
            print('studnet not found')
    except ValueError:
        print('student not found')



def save_student():
    with open('student.txt','w') as f:
        for name,marks in d.items():
            f.write(f'{name}:{marks}\n')
save_student()

def top_student():
    top_student=''
    highest_marks=0
    for name,marks in d.items():
        if highest_marks<marks:
            highest_marks=marks
            top_student=name
            print('--------TOP STUDENT-------')
            print(f'Marks:{top_student} | Name:{highest_marks}')
    


while True:
    print('\n1.Add stuent\n2.view student\n3.Delete student\n4.Exit\n5.Search student\n6.Update marks\n7.Show top student\n8.Exit')
    user=input('enter your choice :')
    if user=='1':
        add_student()

    elif user=='2':
       view_student()
    
    elif user=='3':
        delete_student()
    
    elif user=='4':
        print('exiting...')
        break
    
    elif user=='5':
        search_student()
    
    elif user=='6':
        update_marks()
        print('marks updated')
    
    elif user=='7':
        top_student()

    elif user=='8':
        break

    else:
        print('invalid choice!')
