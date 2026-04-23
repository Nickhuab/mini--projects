import random
questions=[
('what is the capital city of nepal ?','kathmandu'),
('what is the number of bones in human body ?','206'),
('2*4(4/2) ?','16'),
('which is the tallest grass in the world ?','bamboo'),
('who was the first prime minister of nepal ?','bhimsen thapa')
]
random.shuffle(questions)
score=0
print('enter exit to quit')
for i,q in enumerate(questions,start=1):
    print(f'Q{i}. {q[0]}')
    user=input('enter your choice :').lower()
    if user=='exit':
        break
    elif user==q[1]:
        score+=1
        print('correct answer !')
    else:
        print(f'wrong answer ! correct answer is {q[1]}')
print(f'your final score is :{score}/{len(questions)}')
