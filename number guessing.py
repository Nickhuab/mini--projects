import random

num = random.randint(1, 10)
user = int(input("enter number :"))
print(num)
attempts = 3
while num != user and attempts > 0:
    attempts -= 1
    if user > num:
        print(f"{user} is greater try again! attempts left {attempts}")
    elif user < num:
        print(f"{user} is smaller try again! attempts left {attempts}")
    if attempts > 0:
        user = int(input("enter number :"))
if user == num:
        print(f"{user} is a correct guess you won!")
else:
        print("You loose the game! try again!")

