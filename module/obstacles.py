import pygame
import random
from module.settings import *
from module.resources import CACTUS_IMG, PTERO_IMG


class Obstacle():
    def __init__(self, image, pos_x, pos_y):
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hitbox = None
        self.update_hitbox()

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))


class ObstacleList(list):
    def __init__(self):
        self.list = []

    def add(self, obstacle):
        self.list.append(obstacle)

    def update(self, speed):
        for obstacle in self.list:
            obstacle.update(speed)
        for i in reversed(range(len(self.list))):
            if self.list[i].pos_x < - self.list[i].image.get_width():
                del self.list[i]

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        for obstacle in self.list:
            yield obstacle

    def draw(self, screen):
        for obstacle in self.list:
            obstacle.draw(screen)


class Cactus(Obstacle):
    def __init__(self):
        self.index = random.randrange(0, 6)
        super().__init__(CACTUS_IMG[self.index], SCREEN_W, 0)
        if self.index < 3:
            self.pos_y = 224
        else:
            self.pos_y = 212

    def update_hitbox(self):
        self.hitbox = pygame.Rect(
            self.pos_x + 2, self.pos_y + 4,
            self.image.get_width() - 4,
            self.image.get_height() - 2
        )

    def update(self, speed):
        self.pos_x -= speed
        self.update_hitbox()


class Ptero(Obstacle):
    def __init__(self):
        self.index = 0
        super().__init__(PTERO_IMG[0], SCREEN_W,
                         random.randrange(120, 220, 20))

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
