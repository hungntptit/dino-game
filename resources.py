import pygame

pygame.font.init()
SC_FONT = pygame.font.Font("font/press-start.regular.ttf", 12)
MSG_FONT = pygame.font.Font("font/press-start.regular.ttf", 18)

pygame.mixer.init()
JUMP_SND = pygame.mixer.Sound("sounds/jump.wav")
POINT_SND = pygame.mixer.Sound("sounds/point.wav")
DIE_SND = pygame.mixer.Sound("sounds/die.wav")

PATH_IMG = pygame.image.load("images/background/path.png").convert_alpha()
CLOUD_IMG = pygame.image.load("images/background/cloud.png").convert_alpha()
CACTUS_IMG = [pygame.image.load("images/cactus/cactus_0" + str(i) + ".png").convert_alpha()
              for i in range(1, 7)]
BIRD_IMG = [pygame.image.load("images/bird/bird_anim/bird_anim" + str(i) + ".png").convert_alpha()
            for i in range(1, 7)]

RUN_IMG = [pygame.image.load("images/dino/run_anim/run_anim" + str(i) + ".png").convert_alpha()
           for i in range(1, 7)]
DUCK_IMG = [pygame.image.load("images/dino/duck_anim/duck_anim" + str(i) + ".png").convert_alpha()
            for i in range(1, 7)]
JUMP_IMG = pygame.image.load("images/dino/jump/dino_jump.png").convert_alpha()
DIE_IMG = pygame.image.load("images/dino/dino_die.png").convert_alpha()
ICON_IMG = pygame.image.load("images/dino/icon.png").convert_alpha()
RESTART_IMG = pygame.image.load("images/restart.png").convert_alpha()

DESERT = [pygame.image.load("images/background/desert/desert_00" + f"{i:02d}" + ".png").convert_alpha()
          for i in range(0, 5)]
