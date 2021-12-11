import copy as cp
from gl_items_handler import GLItemHandler
from gl_score_handler import GLScoreHandler


class GridLines():
    '''
    GridLines class. Creates and controls an instance of the game.
    '''

    def __init__(self, board_size=10) -> None:
        '''
        Initializes a GridLines game.

        Parameters:
            -board_size (int): desired size of the board.

        '''

        self.__board_size = board_size
        self.__board = [[' ' for j in range(self.__board_size)] for i in range(self.__board_size)]
        self.__symbol_handler = GLItemHandler()
        self.__score_handler = GLScoreHandler()

        self.__current_line = 0
        self.__current_column = 0


    def __verify_place(self) -> bool:
        '''
        Verifies whether it is possible to place the current item at the current position.

        Returns:
            -placeable (bool): whether it is placeable or not.
        '''
        
        item = self.__symbol_handler.get_current_item()
        line, column = self.__current_line, self.__current_column

        placeable = True
        for i in range(len(item)):
            for j in range(len(item[0])):
                if self.__board[i+column][j+line] != ' ' and item[i][j] != None:
                    placeable = False

        return placeable


    def __place_item(self, board=None, temporary=False) -> None:
        '''
        Places an the current item if possible.
        '''

        if board == None:
            board = self.__board

        if self.__verify_place() or temporary:
            item = self.__symbol_handler.get_current_item()
            line, column = self.__current_line, self.__current_column
            
            for i in range(len(item)):
                item[i]

                for j in range(len(item[i])):
                    symbol = item[i][j]

                    if symbol != None:
                        board[i+column] [j+line] = symbol


    def __reset_position(self) -> None:
        self.__current_column = 0
        self.__current_line = 0


    def select_item(self, number) -> None:
        '''
        Selects an item from the pool and refreshes the pool.

        Parameters:
            -number (int): the number of the selected item.
        '''

        self.__symbol_handler.select_item(number)
        self.__symbol_handler.refresh_pool()


    def move_item(self, direction) -> None:
        '''
        Moves an item in a direction.

        Parameters:
            -direction (string): the direction you want to move the item.
        '''

        self.__score_handler.increase_turn()

        item = self.__symbol_handler.get_current_item()

        if direction == 'right':
            if self.__current_line + len(item[0]) < self.__board_size:
                self.__current_line += 1
                return True

        if direction == 'left':
            if self.__current_line > 0:
                self.__current_line -= 1
                return True

        if direction == 'down':
            if self.__current_column + len(item) < self.__board_size:
                self.__current_column += 1
                return True

        if direction == 'up':
            if self.__current_column > 0:
                self.__current_column -= 1
                return True

        if direction == 'place' and self.__verify_place():
            self.__place_item()
            self.__symbol_handler.reset_current_item()
            self.__reset_position()
            self.__score_handler.check_board(self.__board)
            return True

        return False


    def temp_board(self) -> list:
        '''
        Prints a temporary board with current item placed in the current position.

        Returns:
            -string (string): the temporary board's string.
        '''

        temp_board = cp.deepcopy(self.__board)

        self.__place_item(temp_board, True)

        string = 'Board:\n'

        string += '----' * self.__board_size + '-'
        string += '\n'
        for line in temp_board:
            string += '|'

            for block in line:
                string += f' {block} |'

            string += '\n'
            string += '----' * self.__board_size + '-'
            string += '\n'

        string += '\n'
        string += str(self.__symbol_handler)

        return string


    def __str__(self) -> str:
        '''
        Prints the game data.

        Returns:
            -string (string): string of the game's data.
        '''

        string = 'Board:\n'

        string += '----' * self.__board_size + '-'
        string += '\n'
        for line in self.__board:
            string += '|'

            for block in line:
                string += f' {block} |'

            string += '\n'
            string += '----' * self.__board_size + '-'
            string += '\n'

        string += '\n'
        string += str(self.__symbol_handler)

        return string



