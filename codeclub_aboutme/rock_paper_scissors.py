from random import randint

while True:
    player = input('rock(r), paper(p), scissors(s)?')
    #use end= to add space while prining a new line instead of a new line
    print(player, 'vs ', end='')
    chosen = randint(1,3)
    if chosen == 1:
        computer = 'r'
    elif chosen == 2:
        computer = 'p'
    elif chosen == 3:
        computer = 's'
    print(computer)

    if player == computer: 
        print('DRAW')
    elif player == 'r' and computer =='p':
        print('You Lose :)')
    elif player == 'r' and computer =='s':
        print('You win !!')
    elif player == 'p' and computer =='r':
        print('You Win :)')
    elif player == 'p' and computer =='s':
        print('You Lose :)')
    elif player == 's' and computer =='r':
        print('You Lose !!')
    elif player == 's' and computer =='p':
        print('You win !!')