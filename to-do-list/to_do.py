L=[]
def load_task():
    try:
        with open('task.txt','r') as f:
            for line in f:
                task_name,task_status=line.strip().split(':')
    
                status=task_status=='True'
                d={
                    'task':task_name,
                    'done':status
                }
                L.append(d)
    except FileNotFoundError:
        print('File doesnt exist')
load_task() 
     

def save_task():
    with open('task.txt','w') as f:
        for tasks in L:
            f.write(f"{tasks['task']}:{tasks['done']}\n")
save_task()

def add_task():
    if not L:
        print('task doesnt exists')
    user=input('enter new task :')
    for task in L:
        if task['task']==user:
            print('Task already exists')
            return
        
    L.append({'task':user,'done':False})
    print('Task added successfully')
    save_task()

def show_task():
    for i,task in enumerate(L,start=1):
        status='Done' if task['done'] else 'Pending'
        print(f"{i}.{task['task']} ({status})")

def mark_done():
    show_task()
    if not L:
        print('task doesnt exists')
    try:
        num=int(input('enter number of task to mark done :'))
        if num<1 or num>len(L):
            print('invlaid task number')
            return
        L[num-1]['done']=True
        print('task marked as done')

    except ValueError:
        print('invalid inptut')
    save_task()
def delete_task():
    if not L:
        print('task doesnt exists')
    show_task()
    try:
        num=int(input('enter number of task to delete :'))
        if num<1 or num>len(L):
            print('invalid number of task')
            return
        L.pop(num-1)
        print("Task is deleted")
    except ValueError:
        print('Invalid input!! Enter vaild input')
    save_task()

while True:
    print('\n1.Add task\n2.Show tasks\n3.Mark task\n4.Delete task\n5.Exit')
    user=input('enter your choice :')
    if user=='1':
        add_task()

    elif user=='2':
        show_task()

    elif user=='3':
        mark_done()
    
    elif user=='4':
        delete_task()

    elif user=='5':
        break
    else:
        print('Invalid input')

