
class GLScoreHandler():
    '''
    GridLines game score handler.
    '''

    def __init__(self) -> None:
        '''
        Initializes the score handler for the game.
        '''

        self.__score = 0
        self.__turn = 0


    def check_board(self, board) -> None:
        '''
        Checks the game's board and increases score there are completed lines.
        
        Parameters:
            -board (list): the board to be checked.
        '''

        count = 0

        for i in range(len(board)):
            completed = True

            for j in range(len(board[0])):
                if board[i][j] == ' ':
                    completed = False

            if completed: count += 1

        for i in range(len(board[0])):
            completed = True

            for j in range(len(board)):
                if board[j][i] == ' ':
                    completed = False

            if completed: count += 1

        self.__score += 100 * count

        self.__clear_completed_lines(board)


    def increase_turn(self) -> None:
        '''
        Increases the current turn of the game.
        '''
        
        self.__turn += 1


    def __clear_completed_lines(self, board) -> None:
        '''
        Clears the completed lines and columns of a board.

        Parameters:
            -board (list): the board to be cleared.
        '''

        for i in range(len(board)):
            completed = True

            for j in range(len(board[0])):
                if board[i][j] == ' ':
                    completed = False

            if completed:
                for j in range(len(board[0])):
                    board[i][j] = ' '    

        for i in range(len(board[0])):
            completed = True

            for j in range(len(board)):
                if board[j][i] == ' ':
                    completed = False

            if completed:
                for j in range(len(board)):
                    board[j][i] = ' '    


    def __str__(self) -> str:
        '''
        Prints the game's score data.

        Returns:
            -string (string): string of the game's score data.
        '''

        string = f'Score: {self.__score}\n'
        string += f'Turn: {self.__trun}\n'

        return string

