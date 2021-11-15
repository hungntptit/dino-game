from module.resources import SC_FONT
from module.settings import SCREEN_W, GREY

INCREASE_SPEED = 1

POS_X = SCREEN_W - 100
POS_Y = 20


class Score:
    def __init__(self):
        self.points = 0
        self.points_txt = SC_FONT.render(
            "{:06d}".format(self.points // 10), False, GREY)
        f_score = open("data/score.txt")
        self.high_score = int(f_score.readlines()[0])
        f_score.close()
        self.hi_txt = SC_FONT.render(
            "HI {:06d}".format(self.high_score), False, GREY)

    def update(self):
        self.points += INCREASE_SPEED
        self.points_txt = SC_FONT.render(
            "{:06d}".format(self.points // 10), False, GREY)

    def draw(self, screen):
        screen.blit(self.points_txt, (POS_X, POS_Y))
        screen.blit(self.hi_txt, (POS_X - 130, POS_Y))
