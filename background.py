import pygame
import random
from settings import *
from resources import PATH_IMG, CLOUD_IMG, DESERT


class Path:
    def __init__(self):
        self.image = PATH_IMG
        self.w = self.image.get_width()
        self.pos_x1 = 0
        self.pos_x2 = self.w
        self.pos_y = 250

    def update(self, speed):
        self.pos_x1 -= speed
        self.pos_x2 -= speed
        if self.pos_x1 <= -self.w:
            self.pos_x1 = self.w
        if self.pos_x2 <= -self.w:
            self.pos_x2 = self.w

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x1, self.pos_y))
        screen.blit(self.image, (self.pos_x2, self.pos_y))


class Desert:
    def __init__(self):
        self.image = DESERT
        self.w = self.image[0].get_width()
        self.pos_x = [0 for i in range(len(self.image))]
        self.pos_y = 0

    def update(self, speed):
        for i in reversed(range(len(self.image))):
            if i in [0]:
                self.pos_x[i] -= speed
            else:
                self.pos_x[i] -= speed / (i * 3)

            if self.pos_x[i] <= -self.w:
                self.pos_x[i] += self.w

    def draw(self, screen):
        for i in reversed(range(len(self.image))):
            screen.blit(self.image[i], (self.pos_x[i], self.pos_y))
            screen.blit(self.image[i], (self.pos_x[i] +
                                        self.image[0].get_width(), self.pos_y))


class Cloud():
    def __init__(self):
        super().__init__()
        self.image = CLOUD_IMG
        self.rect = self.image.get_rect()
        self.pos_x = SCREEN_W
        self.pos_y = random.randrange(80, 180, 20)
        self.speed = round(random.uniform(0.8, 1.1), 1)

    def update(self):
        self.pos_x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))


class CloudList(list):
    def __init__(self):
        self.list = []

    def add(self, cloud):
        self.list.append(cloud)

    def update(self):
        for cloud in self.list:
            cloud.update()
        for i in reversed(range(len(self.list))):
            if self.list[i].pos_x < - self.list[i].image.get_width():
                del self.list[i]

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        for cloud in self.list:
            yield cloud

    def draw(self, screen):
        for cloud in self.list:
            cloud.draw(screen)
