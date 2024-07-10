import random
grid  = [[0 for x in range(4)] for y in range(4)]

def print_grid():
    for row in grid:
        print(row)

def spawn_title():
    for i in range(8):
        a = random.randint(0,3)
        b = random.randint(0,3)

        while grid[a][b] !=0:
            a = random.randint(0,3)
            b = random.randint(0,3)
        grid[a][b]=1 % 8 + 1


def select_title():
    a = int(input("enter rows: "))
    b = int(input("enter Column: "))

    while a <0 or a>3 or b<0 or b>3 or grid[a][b] ==0:
        print("Invalid input")
        a = int(input("enter rows: "))
        b = int(input("enter Column: "))
    return (a,b)


def play_game():
    spawn_title()
    print_grid()
    first_choice = select_title()
    grid[first_choice[0]][first_choice[1]] = 0
    print_grid()
    second_choice = select_title()
    if grid[second_choice[0]][second_choice[1]]== grid[first_choice[0]][first_choice[1]]:
        print("you found a match. ")
    else:
        print("sorry, try again. ")

play_game()