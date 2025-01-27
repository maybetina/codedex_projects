import random

print('''1) “✊” (Rock). 
2) “✋” (Paper). 
3) “✌️” (Scissors).''')
player = int(input('Choose an option 1-3:'))
computer = random.randint(1,3)

if player == 1:
    print('Player chooses: ✊')
elif player == 2:
    print('Player chooses: ✋')
elif player == 3:
    print('Player chooses: ✌️')
else:
    print('Invalid choice')


if computer == 1:
    print('Computer chooses: ✊')
elif computer == 2:
    print('Computer chooses: ✋')
else:
    print('Computer chooses: ✌️')

if player == 1:
    if player == 1 and computer == 1:
        print("It's a tie!")
    elif player == 1 and computer == 2:
        print("The computer wins!")
    elif player == 1 and computer == 3:
        print("The player wins!")
elif player == 2:
    if player == 2 and computer == 1:
        print("The player wins!")
    elif player == 2 and computer == 2:
        print("It's a tie!")
    elif player == 2 and computer == 3:
        print("The computer wins!")
elif player == 3:
    if player == 3 and computer == 1:
        print("The computer wins!")
    elif player == 3 and computer == 2:
        print("The player wins!")
    elif player == 3 and computer == 3:
        print("It's a tie!")
