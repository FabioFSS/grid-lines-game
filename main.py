import pygame
import sys
from pygame.locals import * 
from drawing_handler import DrawingHandler
from configs import *
from packages.grid_lines import GridLines

game = GridLines(BOARD_SIZE)

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('GridLines')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_handler = DrawingHandler(window, game)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                game.move_item('left')
            
            if event.key == K_d:
                game.move_item('right')
            
            if event.key == K_w:
                game.move_item('up')
           
            if event.key == K_s:
                game.move_item('down')

            if event.key == K_RETURN:
                game.move_item('place')

            if event.key == K_1:
                game.select_item(0)
            
            if event.key == K_2:
                game.select_item(1)
            
            if event.key == K_3:
                game.select_item(2)

    drawing_handler.draw_field()
    drawing_handler.draw_pool()
    pygame.display.update()
