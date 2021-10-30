import os
import random
import pygame
from settings import *
from resources import MSG_FONT, RESTART_IMG, POINT_SND, DIE_SND

from dino import Dino
from scores import Scores
from obstacles import ObstacleList, Cactus, Bird
from background import Path, Desert, Cloud, CloudList


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
        self.obstacles_list = ObstacleList()
        self.cloud_list = CloudList()
        self.path = Path()
        self.desert = Desert()

        # Score
        self.check_score_file()
        self.scores = Scores()

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
                    # reset game
                    self.reset()

    def check_score_file(self):
        if os.path.exists("score.txt"):
            f_score = open("score.txt", "r+")
            if not f_score.read():
                f_score.write("0")
            f_score.close()
        else:
            f_score = open("score.txt", "w")
            f_score.write("0")
            f_score.close()

    def update_speed(self):
        # Increase speed right after start
        if self.speed <= 3:
            self.speed += 0.018
        # Increase speed every 100 points
        if (
            self.scores.points > 0
            and self.scores.points % 1000 == 0
            and self.speed < 15
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
        f_score = open("score.txt", "r+")
        old_score = int(f_score.readlines()[0])
        f_score.close()
        new_score = self.scores.points // 10
        if new_score > old_score:
            f_score = open("score.txt", "w")
            f_score.write("%s" % new_score)
            f_score.close()

    def add_objects(self):
        # Add obstacles randomly
        if self.this_time - self.ob_last_time > random.randrange(
            self.ob_min_distance, self.ob_max_distance, 100
        ):
            self.ob_last_time = self.this_time
            if random.randrange(0, 100) < 80:
                self.obstacles_list.add(Cactus())
            else:
                self.obstacles_list.add(Bird())
        # Add clouds randomly
        if (
            self.this_time -
                self.cl_last_time > random.randrange(3000, 8001, 1000)
            and len(self.cloud_list) < 4
        ):
            self.cl_last_time = self.this_time
            self.cloud_list.add(Cloud())

    def check_collision(self):
        for obstacle in self.obstacles_list:
            if self.dino.hitbox_head.colliderect(obstacle.hitbox) \
                    or self.dino.hitbox_body.colliderect(obstacle.hitbox):
                return True
        return False

    def update_all(self, keys):
        self.this_time = pygame.time.get_ticks()
        self.add_objects()
        self.update_speed()
        # self.cloud_list.update()
        # self.path.update(self.speed)

        self.desert.update(self.speed)

        self.obstacles_list.update(self.speed)
        self.dino.update(keys)
        self.scores.update()
        if self.check_collision():
            pass
            DIE_SND.play()
            self.is_over = True
            self.dino.die()
            self.update_high_score()

    def draw_screen(self):
        SCREEN.fill('black')

        if not self.is_start:
            SCREEN.fill(BG)
            self.desert.draw(SCREEN)
            SCREEN.blit(self.start_text, self.start_text_rect)
        else:
            # self.cloud_list.draw(SCREEN)
            # self.path.draw(SCREEN)

            self.desert.draw(SCREEN)

            self.obstacles_list.draw(SCREEN)
            if self.is_over:
                SCREEN.blit(self.game_over_text, self.game_over_rect)
                SCREEN.blit(RESTART_IMG, self.restart_rect)
        self.dino.draw(SCREEN)
        self.scores.draw(SCREEN)

        pygame.display.update()
        self.clock.tick(FPS)
