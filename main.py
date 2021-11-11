import pygame
from module.game_funtion import GameFuntion
from module.resources import ICON_IMG


pygame.display.set_caption("Dino Game")
pygame.display.set_icon(ICON_IMG)

game = GameFuntion()

while game.is_running:
    game.check_events()
    if game.is_start and not game.is_over:
        game.update_all(pygame.key.get_pressed())
    game.draw_screen()

pygame.quit()
