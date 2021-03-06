import pygame
from configs import *
import random as rd
import copy as cp

class ItemDrawer():
    '''
    A drawer for a selected item.
    '''

    def __init__(self, window, item, color) -> None:
        '''
        Initializes de item drawer.
        
        Parameters:
            -item (tuple): the item to be drawn.
            -color (tuple): the color of the item.
        '''

        self.__window = window
        self.__color = BLOCK_COLOR
        
        self.__item = cp.deepcopy(item)
        self.__resize_item()

    
    def draw(self, x, y, width, height) -> None:
        '''
        Draws the item with pygame.
        '''

        # drawing inside squares
        for i in range(3):
            for j in range(3):
                square_height = height // 3
                square_width = width // 3
                square_x = x + square_width * j
                square_y = y + square_height * i

                position = (square_x, square_y, square_width, square_height)
                if self.__item[i][j] != None:
                    pygame.draw.rect(self.__window, self.__color, position)


    def __resize_item(self) -> None:
        '''
        Resizes the item to a 3x3 matrix.
        '''

        resized = False
        while not resized:
            if len(self.__item) < 3:
                self.__item.append([None, None, None])

            else:
                for i in range(len(self.__item)):
                    if len(self.__item[i]) < 3:
                        self.__item[i].append(None)
                
                    else: 
                        resized = True



class DrawingHandler():
    '''
    A handler for drawing the objects from the game on the screen with pygame.
    '''

    def __init__(self, window, game) -> None:
        '''
        Initializes the drawing handler.

        Parameters:
            -window (pygame display): the window where the objets will be drawn.
        '''

        self.__window = window
        self.__game = game


    def __random_color(self) -> tuple:
        '''
        Returns a random color.

        Returns:
            -chosen_color (tuple): a random color from a tuple of colors.
        '''
        
        colors = (
                (128, 0, 128),
                (128, 128, 0),
                (0, 128, 128),
                (0, 0, 128),
                (128, 0, 0),
                (0, 128, 0)
                )

        chosen_color = rd.choice(colors)

        return chosen_color


    def draw_field(self) -> None:
        '''
        Draws the field of the game.
        '''

        # defining colors
        back_color = FIELD_COLOR
        line_color = LINE_COLOR
        block_color = BLOCK_COLOR
        mask_color = MASK_COLOR

        # drawing field background
        padding = 50
        field_width = WINDOW_WIDTH - padding - 200
        field_height = WINDOW_HEIGHT - padding - 100
        field_x = padding/2
        field_y = padding/2

        position = (field_x, field_y, field_width, field_height)

        pygame.draw.rect(self.__window, back_color, position)

        field = self.__game.get_board()

        if self.__game.get_current_item() != None:
            item_mask = self.__game.get_item_mask()

        # drawing board and items on the board
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                block = field[i][j]
    
                if block != ' ':

                    width = (field_width / BOARD_SIZE)
                    height = (field_height / BOARD_SIZE)
                    x = j * width + field_x
                    y = i * height + field_y

                    position = (x, y, width, height)

                    pygame.draw.rect(self.__window, block_color, position)        
                
                if self.__game.get_current_item() != None:
                    mask_block = item_mask[i][j]

                    if mask_block != ' ':
                        width = (field_width / BOARD_SIZE)
                        height = (field_height / BOARD_SIZE)
                        x = j * width + field_x
                        y = i * height + field_y

                        position = (x, y, width, height)

                        pygame.draw.rect(self.__window, mask_color, position)        

        # drawing horizontal lines
        for i in range(BOARD_SIZE+1):
            line_x1 = field_x
            line_y1 = field_y + (field_height / BOARD_SIZE) * i
            first_point = (line_x1, line_y1)

            line_x2 = field_width + field_x
            line_y2 = field_y + (field_height / BOARD_SIZE) * i
            second_point = (line_x2, line_y2)

            weight = 5

            pygame.draw.line(self.__window, line_color, first_point, second_point, weight)

        # drawing vertical lines
        for i in range(BOARD_SIZE+1):
            line_x1 = field_x + (field_width / BOARD_SIZE) * i
            line_y1 = field_y
            first_point = (line_x1, line_y1)

            line_x2 = field_x + (field_width / BOARD_SIZE) * i
            line_y2 = field_height + field_y
            second_point = (line_x2, line_y2)

            weight = 5

            pygame.draw.line(self.__window, line_color, first_point, second_point, weight)


    def draw_pool(self):
        '''
        Draws the game's pool.
        '''

        pool = self.__game.get_pool()

        pool_color = BACKGROUND_COLOR
        padding = 50
        pool_x = (WINDOW_WIDTH - padding - 200) + (padding)
        pool_y = padding/2
        pool_width = WINDOW_WIDTH - pool_x - padding/2
        pool_height = WINDOW_HEIGHT - padding

        position = (pool_x, pool_y, pool_width, pool_height)

        pygame.draw.rect(self.__window, pool_color, position)

        for i in range(POOL_SIZE):
            # color = self.__random_color()
            inside_padding = 25
            item_color = (128, 0, 0)
            
            x = pool_x + inside_padding/2
            y = (padding/2) + (pool_height/POOL_SIZE) * i + (inside_padding/2)
            width = pool_width - inside_padding
            height = (pool_height/POOL_SIZE) - inside_padding

            item = ItemDrawer(self.__window, pool[i], item_color)
            item.draw(x, y, width, height)


    def draw_score(self):
        '''
        Draws the game score and turn.
        '''
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        score_text = font.render(f'Score: {self.__game.get_score()}    Turn: {self.__game.get_turn()}', True, LINE_COLOR)
        score_text_rectangle = score_text.get_rect()
        score_text_rectangle.center = (175, WINDOW_HEIGHT-50)

        self.__window.blit(score_text, score_text_rectangle)

