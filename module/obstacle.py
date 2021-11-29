import pygame
import random
from module.settings import *
from module.resources import CACTUS_IMG, PTERO_IMG, VIRUS_IMG
from module.object import Object


class Cactus(Object):
    def __init__(self):
        self.index = random.randrange(0, len(CACTUS_IMG))
        super().__init__(CACTUS_IMG[self.index], SCREEN_W, 0)
        if self.index < 3:
            self.pos_y = 226
        else:
            self.pos_y = 212
        self.hitbox = None

    def update_hitbox(self):
        self.hitbox = pygame.Rect(
            self.pos_x + 2, self.pos_y + 4,
            self.image.get_width() - 4,
            self.image.get_height() - 2
        )

    def update(self, speed):
        self.pos_x -= speed
        self.update_hitbox()


class Ptero(Object):
    def __init__(self):
        self.index = 0
        super().__init__(PTERO_IMG[0], SCREEN_W,
                         random.randrange(120, 220, 20))
        self.hitbox = None

    def update_hitbox(self):
        self.hitbox = pygame.Rect(
            self.pos_x + 16, self.pos_y + 24,
            self.image.get_width() - 30,
            self.image.get_height() - 46
        )

    def update(self, speed):
        self.pos_x -= speed
        self.update_hitbox()
        self.image = PTERO_IMG[int(self.index) % 6]
        self.index += 0.1
        if self.index >= 6:
            self.index = 0


class Virus(Object):
    def __init__(self):
        self.index = random.randrange(0, len(VIRUS_IMG))
        super().__init__(VIRUS_IMG[self.index], SCREEN_W,
                         random.randrange(120, 220, 20))
        self.hitbox = None

    def update_hitbox(self):
        self.hitbox = pygame.Rect(
            self.pos_x + 6, self.pos_y + 6,
            self.image.get_width() - 12,
            self.image.get_height() - 12
        )

    def update(self, speed):
        self.pos_x -= speed
        self.update_hitbox()
