import pygame
import sys
import time as tm
from pygame.locals import * 
from drawing_handler import DrawingHandler
from configs import *
from packages.grid_lines import GridLines


game = GridLines(BOARD_SIZE, POOL_SIZE)

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('GridLines')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_handler = DrawingHandler(window, game)


last_pressed = tm.time()
interval = 0.05

while True:
    clock.tick(60)
    window.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                game.move_item('place')

            if event.key == K_1:
                game.select_item(0)
            
            if event.key == K_2:
                game.select_item(1)
            
            if event.key == K_3:
                game.select_item(2)

        if tm.time() - last_pressed > interval:
            if pygame.key.get_pressed()[K_w]:
                game.move_item('up')
                last_pressed = tm.time()

            if pygame.key.get_pressed()[K_s]:
                game.move_item('down')
                last_pressed = tm.time()

            if pygame.key.get_pressed()[K_a]:
                game.move_item('left')
                last_pressed = tm.time()
            
            if pygame.key.get_pressed()[K_d]:
                game.move_item('right')
                last_pressed = tm.time()

    drawing_handler.draw_field()
    drawing_handler.draw_pool()
    drawing_handler.draw_score()

    game_over = game.check_game_over()
    if game_over:
        font = pygame.font.Font('freesansbold.ttf', 64)
        game_over_text = font.render('Game Over', True, (0, 0, 0))
        game_over_text_rectangle = game_over_text.get_rect()
        game_over_text_rectangle.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        font = pygame.font.Font('freesansbold.ttf', 32)
        continue_text = font.render('press "r" to continue', True, (0, 0, 0))
        continue_text_rectangle = continue_text.get_rect()
        continue_text_rectangle.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+150)


        pygame.draw.rect(window, GAME_OVER_COLOR, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        window.blit(game_over_text, game_over_text_rectangle)
        window.blit(continue_text, continue_text_rectangle)

        if pygame.key.get_pressed()[K_r]:
            game = GridLines(BOARD_SIZE, POOL_SIZE)
            drawing_handler = DrawingHandler(window, game)
            game_over = False

    pygame.display.update()
