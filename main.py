import pygame
import sys
from pygame.locals import * 
from drawing_handler import DrawingHandler
from configs import *
from packages.grid_lines import GridLines

game = GridLines(BOARD_SIZE)

pygame.init()
pygame.display.set_caption('GridLines')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_handler = DrawingHandler(window, game)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    drawing_handler.draw_field()
    drawing_handler.draw_pool()
    pygame.display.update()
    