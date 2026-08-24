import random

rock = 1
paper = 0
scissor = -1

game_choice = random.choice([-1,0,1])

print('''
1. rock
0. paper
-1. scissor
''')
user_choice = int(input("choose: "))

user_win = [(1,0),(0,-1),(-1,1)]
game_win = [(1,-1),(0,1),(-1,0)]

move = (game_choice, user_choice)

if move in user_win:
    print("You Won!!")
elif move in game_win:
    print("You lose.")
else:
    print("Draww")