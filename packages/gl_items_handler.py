import numpy as np
import random as rd

class GLItemHandler():
    '''
    GridLines game items handler. Manages and generates all the items for the game.
    '''

    def __init__(self, char='o', pool_size=3) -> None:
        '''
        Initializes the handler for items that can appear in the game.

        Parameters:
            -char (str): the char that the items will use.
            -pool_size (int): the size of the game's pool.
        '''

        self.__char = char
        self.__pool_size = pool_size

        self.__items = [
        [[self.__char, self.__char, self.__char]],

        [[self.__char, self.__char],
        [self.__char, self.__char]],

        [[self.__char, None],
        [self.__char, None],
        [self.__char, self.__char]],

        [[None, self.__char],
        [None, self.__char],
        [self.__char, self.__char]], 

        [[self.__char, None],
        [self.__char, self.__char],
        [None, self.__char]],

        [[None, self.__char],
        [self.__char, self.__char],
        [self.__char, None]],

        [[None, self.__char, None],
        [self.__char, self.__char, self.__char]]
        ]

        self.__pool = [self.__random_item() for i in range(self.__pool_size)]
        self.__current_item = None


    def __random_item(self) -> list:
        '''
        Selects a random item from the possible items.

        Returns:
            -choice(list): a random item.
        '''

        new_item = rd.choice(self.__items)

        for i in range(rd.randint(0, 4)):
            direction = rd.choice(['right', 'left'])
            new_item = self.__rotate_item(new_item, direction)

        return new_item


    def __rotate_item(self, item, direction) -> list:
        '''
        Rotates and item.
        
        Parameters:
            -item (list): the item you want to rotate.
            -direction (string): the direction that the item will be rotated in.

        Returns:
            -transposed (list): the rotated item.
        '''

        if direction == 'right':
            reversed_item = [line[::-1] for line in item]
            transposed = np.transpose(reversed_item)
            reversed_item = [line[::-1] for line in transposed]
            transposed = np.transpose(reversed_item)
            reversed_item = [line[::-1] for line in transposed]
            transposed = np.transpose(reversed_item)

        elif direction == 'left':
            reversed_item = [line[::-1] for line in item]
            transposed = np.transpose(reversed_item)

        return list(list(item) for item in transposed)


    def select_item(self, number) -> list:
        '''
        Selects an item from the pool.

        Parameters:
            -number (int): the number of the desired item.

        Returns:
            -current_item (list): the selected item.
        '''

        self.__current_item = self.__pool.pop(number)
        current_item = self.get_current_item()

        return current_item


    def refresh_pool(self) -> None:
        '''
        Adds new items into the missing places of the pool.
        '''

        while len(self.__pool) < self.__pool_size:
            new_item = self.__random_item()
            self.__pool.append(new_item)


    def reset_current_item(self) -> None:
        '''
        Resets the current item to None.
        '''

        self.__current_item = None


    def get_pool(self) -> list:
        '''
        Returns the item pool.
        
        Returns:
            -pool (list): the current item pool.
        '''

        pool = self.__pool

        return pool


    def get_current_item(self) -> list:
        '''
        Returns the current item.

        Returns:
            -current_item (list): the currently selected item.
        '''
        
        current_item = self.__current_item

        return current_item


    def __str__(self) -> str:
        '''
        Prints the items' data.

        Returns:
            -string (string): string of the items' data.
        '''

        string = 'Pool:\n'

        height = max(len(item) for item in self.__pool)
        for i in range(height):
            for item in self.__pool:
                if len(item) > i:
                    item_string = str(item[i])
                    string += f'{item_string:<20}'
                
                else:
                    item_string = ' '
                    string += f'{item_string:<20}'
                    
            string += '\n'

        if self.__current_item != None:
            string += '\nCurrent item:\n'

            for line in self.__current_item:
                item_string = str(line)
                string += f'{item_string:<20}\n'

        return string
