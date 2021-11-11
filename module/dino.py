import pygame
from module.resources import JUMP_IMG, DIE_IMG, RUN_IMG, DUCK_IMG, JUMP_SND

DINO_POS_X = 60
DINO_POS_Y = 210

RUN_SPD = 0.1
VEL = 5.25
GRAVITY = 0.15


class Dino():
    def __init__(self):
        self.image = JUMP_IMG
        self.pos_x = DINO_POS_X
        self.pos_y = DINO_POS_Y

        self.is_jumping = False
        self.is_falling = False
        self.is_running = False
        self.is_ducking = False

        self.index = 0
        self.velocity = VEL
        self.run_speed = RUN_SPD

        self.hitbox_head = None
        self.hitbox_body = None
        self.update_hitbox()

    def update_hitbox(self):
        if self.is_ducking:
            self.hitbox_head = pygame.Rect(
                self.pos_x + 38, self.pos_y + 28, 22, 14
            )
            self.hitbox_body = pygame.Rect(
                self.pos_x + 8, self.pos_y + 32, 24, 18
            )
        else:
            self.hitbox_head = pygame.Rect(
                self.pos_x + 32, self.pos_y + 8, 22, 14
            )
            self.hitbox_body = pygame.Rect(
                self.pos_x + 14, self.pos_y + 28, 24, 24
            )

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def die(self):
        self.image = DIE_IMG

    def run(self):
        self.image = RUN_IMG[int((self.index)) % 6]
        self.update_hitbox()
        self.index += self.run_speed
        if self.index >= 6:
            self.index = 0

    def duck(self):
        self.image = DUCK_IMG[int((self.index)) % 6]
        self.update_hitbox()
        self.index += self.run_speed
        if self.index >= 6:
            self.index = 0

    def jump(self):
        self.image = JUMP_IMG
        self.update_hitbox()
        if self.is_jumping:
            self.pos_y -= self.velocity
            self.velocity -= GRAVITY
            if self.velocity <= 0:
                self.velocity = 0
                self.is_falling = True
                self.is_jumping = False
        elif self.is_falling:
            self.pos_y += self.velocity
            self.velocity += GRAVITY
            if self.pos_y >= DINO_POS_Y:
                self.pos_y = DINO_POS_Y
                self.velocity = VEL
                self.is_running = True
                self.is_falling = False

    def check_events(self, keys):
        if not (self.is_jumping or self.is_falling):
            if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and self.is_running:
                self.is_running = False
                self.is_ducking = False
                self.is_jumping = True
                JUMP_SND.play()
            elif keys[pygame.K_DOWN]:
                if self.is_running or self.is_ducking:
                    self.is_running = False
                    self.is_ducking = True
                    self.is_jumping = False
            else:
                self.is_running = True
                self.is_ducking = False
                self.is_jumping = False

    def update(self, keys):
        self.check_events(keys)
        if self.is_jumping or self.is_falling:
            self.jump()
        elif self.is_running:
            self.run()
        elif self.is_ducking:
            self.duck()
