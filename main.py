import pygame
from game_funtion import GameFuntion


game = GameFuntion()

while game.is_running:
    game.check_events()
    if game.is_start and not game.is_over:
        game.update_all(pygame.key.get_pressed())
    game.draw_screen()

pygame.quit()
