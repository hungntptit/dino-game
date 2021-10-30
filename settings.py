import pygame

SCREEN_W = 800
SCREEN_H = 300
SCREEN = pygame.display.set_mode([SCREEN_W, SCREEN_H])

GREY = (80, 80, 80)
BG = (240, 240, 240)

FPS = 120

pygame.display.set_caption("Dino Game")
pygame.display.set_icon(pygame.image.load(
    "images/dino/icon.png").convert_alpha())
