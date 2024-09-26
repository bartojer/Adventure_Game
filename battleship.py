'''
Battleship
'''
import random

'''
x1 = int(input('First x coordinate: '))
y1 = int(input('First y coordinate: '))
x2 = int(input('Second x coordinate: '))
y2 = int(input('Second y coordinate: '))
x3 = int(input('Third x coordinate: '))
y3 = int(input('Third y coordinate: '))
x4 = int(input('Fourth x coordinate: '))
y4 = int(input('Fourth y coordinate: '))
'''

x1 = random.randint(1,8)
y1 = random.randint(1,8)
x2 = random.randint(1,8)
y2 = random.randint(1,8)
x3 = random.randint(1,8)
y3 = random.randint(1,8)
x4 = random.randint(1,8)
y4 = random.randint(1,8)
x5 = random.randint(1,8)
y5 = random.randint(1,8)
x6 = random.randint(1,8)
y6 = random.randint(1,8)
x7 = random.randint(1,8)
y7 = random.randint(1,8)
x8 = random.randint(1,8)
y8 = random.randint(1,8)

ships = [f'{x1},{y1}', f'{x2},{y2}', f'{x3},{y3}', f'{x4},{y4}', 
         f'{x5},{y5}', f'{x6},{y6}', f'{x7},{y7}', f'{x8},{y8}',]
shots_fired = []
hits = []


while True:

    x1 = random.randint(1,8)
    y1 = random.randint(1,8)
    x2 = random.randint(1,8)
    y2 = random.randint(1,8)
    x3 = random.randint(1,8)
    y3 = random.randint(1,8)
    x4 = random.randint(1,8)
    y4 = random.randint(1,8)
    x5 = random.randint(1,8)
    y5 = random.randint(1,8)
    x6 = random.randint(1,8)
    y6 = random.randint(1,8)
    x7 = random.randint(1,8)
    y7 = random.randint(1,8)
    x8 = random.randint(1,8)
    y8 = random.randint(1,8)

    ships = [f'{x1},{y1}', f'{x2},{y2}', f'{x3},{y3}', f'{x4},{y4}', 
            f'{x5},{y5}', f'{x6},{y6}', f'{x7},{y7}', f'{x8},{y8}',]
    shots_fired = []
    hits = []


    print(ships)

    done = False
    while not done:

        print('Where do you fire?')
        x_coordinate = int(input('x coordinate: '))
        y_coordinate = int(input('y coordinate: '))
        fire = f'{x_coordinate},{y_coordinate}'


        while x_coordinate < 1 or x_coordinate > 8 or y_coordinate < 1 or y_coordinate > 8:
            print('Invalid coordinate. Try again (enter integer 1-5)')
            x_coordinate = int(input('x coordinate: '))
            y_coordinate = int(input('y coordinate: '))

        fire = f'{x_coordinate},{y_coordinate}'

        if fire in shots_fired:
            print('You have already fired there. Where do you fire?')
            x_coordinate = int(input('x coordinate: '))
            y_coordinate = int(input('y coordinate: '))

            while x_coordinate < 1 or x_coordinate > 8 or y_coordinate < 1 or y_coordinate > 8:
                print('Invalid coordinate. Try again (enter integer 1-5)')
                x_coordinate = int(input('x coordinate: '))
                y_coordinate = int(input('y coordinate: '))
        else:
            if fire in ships:
                hits.append(fire)
                print('Hit')
            else:
                print('Miss')
            shots_fired.append(fire)

        shots_fired.append(fire)

        if len(hits) == len(ships):
            print('Victory!')
            done = True
    
    again = input('Do you want to play again?: ').lower()
    if again != 'yes':
        break