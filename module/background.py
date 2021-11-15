import random
from module.resources import DESERT_IMG, CLOUD_IMG
from module.settings import SCREEN_W
from module.object import Object


class Desert:
    def __init__(self):
        self.image = DESERT_IMG
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
            screen.blit(self.image[i], (self.pos_x[i] + self.w, self.pos_y))


class Cloud(Object):
    def __init__(self):
        super().__init__(CLOUD_IMG[random.randrange(
            0, (len(CLOUD_IMG)))], SCREEN_W, random.randrange(40, 130, 10))
        self.speed = round(random.uniform(0.8, 1.1), 1)

    def update(self):
        self.pos_x -= self.speed
