import os
import random
import pygame
from module.settings import *
from module.resources import MSG_FONT, RESTART_IMG, POINT_SND, DIE_SND
from module.dino import Dino
from module.score import Score
from module.obstacle import Cactus, Ptero
from module.background import Desert, Cloud
from module.object import ObjectList


class GameFuntion:
    def __init__(self):
        self.reset()

    def reset(self):
        # Time
        self.clock = pygame.time.Clock()
        self.ob_min_distance = 1000
        self.ob_max_distance = 6000
        self.this_time = self.ob_last_time = self.cl_last_time = pygame.time.get_ticks()

        # Control
        self.speed = 0
        self.is_start = False
        self.is_over = False
        self.is_running = True

        # Objects
        self.dino = Dino()
        self.obstacle_list = ObjectList()
        self.cloud_list = ObjectList()
        self.background = Desert()

        # Score
        self.check_score_file()
        self.score = Score()

        # Text
        self.start_text = MSG_FONT.render("PRESS SPACE TO START", True, GREY)
        self.start_text_rect = self.start_text.get_rect(
            center=(SCREEN_W // 2, SCREEN_H // 3)
        )
        self.game_over_text = MSG_FONT.render("G A M E  O V E R", True, GREY)
        self.game_over_rect = self.game_over_text.get_rect(
            center=(SCREEN_W // 2, SCREEN_H // 3)
        )

        # Image
        self.restart_rect = RESTART_IMG.get_rect(
            center=(SCREEN_W // 2, SCREEN_H // 2))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if not self.is_start:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.is_start = True
            if self.is_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.reset()

    def check_score_file(self):
        if os.path.exists("data/score.txt"):
            f_score = open("data/score.txt", "r+")
            if not f_score.read():
                f_score.write("0")
            f_score.close()
        else:
            f_score = open("data/score.txt", "w")
            f_score.write("0")
            f_score.close()

    def update_speed(self):
        # Increase speed right after start
        if self.speed <= 3:
            self.speed += 0.018
        # Increase speed every 100 points
        if (
            self.score.points > 0
            and self.score.points % 1000 == 0
            and self.speed < 16
        ):
            POINT_SND.play()

            if self.ob_min_distance > 500:
                self.ob_min_distance -= 100
            if self.ob_max_distance > 2400:
                self.ob_max_distance -= 200

            if self.speed < 8:
                self.speed += 0.5
                self.dino.run_speed += 0.002
            else:
                self.speed += 0.1

    def update_high_score(self):
        f_score = open("data/score.txt", "r+")
        old_score = int(f_score.readlines()[0])
        f_score.close()
        new_score = self.score.points // 10
        if new_score > old_score:
            f_score = open("data/score.txt", "w")
            f_score.write("%s" % new_score)
            f_score.close()

    def add_objects(self):
        # Add obstacles randomly
        ratio = 90 if self.score.points < 5000 else 60
        if self.this_time - self.ob_last_time > random.randrange(
            self.ob_min_distance, self.ob_max_distance, 100
        ):
            self.ob_last_time = self.this_time
            if random.randrange(0, 100) < ratio:
                self.obstacle_list.add(Cactus())
            else:
                self.obstacle_list.add(Ptero())
        # Add clouds randomly
        if (
            self.this_time -
                self.cl_last_time > random.randrange(3000, 8001, 1000)
            and len(self.cloud_list) < 4
        ):
            self.cl_last_time = self.this_time
            self.cloud_list.add(Cloud())

    def check_collision(self):
        for obstacle in self.obstacle_list:
            if self.dino.hitbox_head.colliderect(obstacle.hitbox) \
                    or self.dino.hitbox_body.colliderect(obstacle.hitbox):
                return True
        return False

    def update_all(self, keys):
        self.this_time = pygame.time.get_ticks()
        self.add_objects()
        self.update_speed()
        self.background.update(self.speed)
        self.cloud_list.update_cl()
        self.obstacle_list.update_ob(self.speed)
        self.dino.update(keys)
        self.score.update()
        if self.check_collision():
            DIE_SND.play()
            self.is_over = True
            self.dino.die()
            self.update_high_score()

    def draw_screen(self):
        SCREEN.fill(BG)
        if not self.is_start:
            self.background.draw(SCREEN)
            SCREEN.blit(self.start_text, self.start_text_rect)
        else:
            self.cloud_list.draw(SCREEN)
            self.background.draw(SCREEN)
            self.obstacle_list.draw(SCREEN)
            if self.is_over:
                SCREEN.blit(self.game_over_text, self.game_over_rect)
                SCREEN.blit(RESTART_IMG, self.restart_rect)
        self.dino.draw(SCREEN)
        self.score.draw(SCREEN)
        pygame.display.update()
        self.clock.tick(FPS)
