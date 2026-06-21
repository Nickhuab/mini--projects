expense=[]

def load_expense():
    try:
        with open('expense.txt','r') as f:
            for line in f:
                catagory,amt=line.strip().split(':')
                d={
                    'catagory':catagory,
                    'amount':float(amt)
                }
                expense.append(d)
    except FileNotFoundError:
        pass
load_expense()

def save_expense():
    with open('expense.txt','w') as f:
        for item in expense:
            f.write(f"{item['catagory']}:{item['amount']}\n")
save_expense()


def Add_expense():
    user=input('enter catagory of expense :')
    amt=float(input('Enter amount spent :'))
    
    expense.append({'catagory':user,'amount':amt})
    print('expense added successfully')
    save_expense()
    
def show_expense():
    for i,amount in enumerate(expense,start=1):
        print(f"{i}.{amount['catagory']} - {amount['amount']}") 

def Total_expense():
    total=0
    for item in expense:
        total=total+item['amount']
    print(f'Total amount spent: Rs.{total}')

def summary():
    summ={}

    for item in expense:
        cat=item['catagory']
        amt=item['amount']
        if cat in summ:
            summ[cat]+=amt
        else:
            summ[cat]=amt
 
    for cat,total in summ.items():
        print(f'{cat} : {total}')

def Delete_expense():
    try:
        for i,items in enumerate(expense,start=1):
            print(f'{i}.{items['catagory']}')

        while True:
            user=int(input('enter number of catagory to delete :'))
            if user<1 or user>len(expense):
                print('invalid input')
                continue
            else:
                expense.pop(user-1)
                print('expense deleted successfully')
                break
        save_expense()
    except ValueError:
        pass

while True:
    print('\n1.Add expense\n2.View expense\n3.Total amount spent\n4.Catagory summary\n5.Delete expense\n6.Exit')
    user=input('enter your choice :')

    if user=='1':
        Add_expense()
    
    elif user=='2':
        show_expense()

    elif user=='3':
        Total_expense()

    elif user=='4':
        summary()

    elif user=='5':
        Delete_expense()

    elif user=='6':
        break

    else:
        print('Invalid input!!')


