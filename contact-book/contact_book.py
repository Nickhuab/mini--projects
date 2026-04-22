contacts={'raj':97536452,
        'bikash':98704747,
        'riya':9898776,
        'maya':986277,
        'priya':987678
        }
while True:
    user=input('1.Add contact\n2.search contact\n3.delete contact\n4.show all contacts\nplease type exit to quit\nEnter your choice :')
    if user=='1':
        name=input('enter new name :').lower()
        numb=input('enter new contact :')
        if name in contacts:
            print(f'{name} already exists please enter new name')
        else:
            contacts[name]=numb
            print(f'{name}:{numb} is added')
            print(contacts)
    elif user=='2':
        s=input('enter name to search :').lower()
        if s in contacts:
            print(f'{s}:{contacts[s]}')
        else:
            print(f'{s} doesnt exist')
    elif user=='3':
        d=input('enter name to delete :').lower()
        if d in contacts:
            print(f'{d}:{contacts.pop(d,None)} is removed')
            print(contacts)
    elif user=='4':
        print(contacts)
        for name in contacts:
            print(f'{name}: {contacts[name]}')
    elif user=='exit':
        break
    else:
        print('Invalid')

