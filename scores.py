from settings import *
from resources import *

INCREASE_SPEED = 1

POS_X = SCREEN_W - 100
POS_Y = 20


class Scores:
    def __init__(self):
        self.points = 0
        self.point_txt = SC_FONT.render(
            "{:06d}".format(self.points // 10), False, GREY)
        f_score = open("score.txt")
        self.high_score = int(f_score.readlines()[0])
        f_score.close()
        self.hi_txt = SC_FONT.render(
            "HI {:06d}".format(self.high_score), False, GREY)

    def update(self):
        self.point_txt = SC_FONT.render(
            "{:06d}".format(self.points // 10), False, GREY)
        self.points += INCREASE_SPEED

    def draw(self, screen):
        screen.blit(self.point_txt, (POS_X, POS_Y))
        screen.blit(self.hi_txt, (POS_X - 130, POS_Y))
