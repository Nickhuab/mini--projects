
import random
choices=['rock','paper','scissors']

attempts=3
user_score=0
computer_score=0

while attempts>0:
    computer=random.choice(choices)
    user=input("enter your choice :")
    if user in choices:
        attempts-=1
        if user=='rock' and computer=='scissors' or user=='paper' and computer=='rock' or user=='scissors' and computer=='paper':
            print(f'computer={computer} vs you={user},{user} won this time!\nattemts left={attempts}')
            user_score+=1
        else:
             print(f'computer={computer} vs you={user} {computer} won this time!\nattemts left={attempts}')
             computer_score+=1
    else:
        print('invalid.. please choose among rock, paper or scissors')

print('-------------FINAL RESULT-------------')
print(f'Your score is {user_score}')
print(f'computer score is {computer_score}')
if computer_score>user_score:
     print('So Computer is the winner!!')
else:
     print('SO You are the winner!!')
