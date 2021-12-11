import os

from grid_lines import GridLines

if __name__ == '__main__':
    game = GridLines(7)

    while True:
        os.system('cls')
        
        print(game)

        choice = int(input('Escolha um item:'))
        game.select_item(choice)

        placed = False
        while not placed:
            os.system('cls')
            print(game.temp_board())

            move = None
            while move not in ['w', 'a', 's', 'd', 'p']:
                move = input('Faça um movimento: ')

            if move == 'w':
                game.move_item('up')

            if move == 'a':
                game.move_item('left')
            
            if move == 's':
                game.move_item('down')

            if move == 'd':
                game.move_item('right')

            if move == 'p':
                placed = game.move_item('place')
