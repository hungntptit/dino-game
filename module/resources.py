import pygame

pygame.font.init()
SC_FONT = pygame.font.Font("data/font/press-start.regular.ttf", 12)
MSG_FONT = pygame.font.Font("data/font/press-start.regular.ttf", 18)

pygame.mixer.init()
JUMP_SND = pygame.mixer.Sound("data/sounds/jump.wav")
POINT_SND = pygame.mixer.Sound("data/sounds/point.wav")
DIE_SND = pygame.mixer.Sound("data/sounds/die.wav")

CACTUS_IMG = [pygame.image.load("data/images/cactus/cactus_0" + str(i) + ".png").convert_alpha()
              for i in range(1, 7)]
PTERO_IMG = [pygame.image.load("data/images/ptero/ptero_anim/ptero_anim" + str(i) + ".png").convert_alpha()
             for i in range(1, 7)]

RUN_IMG = [pygame.image.load("data/images/dino/run_anim/run_anim" + str(i) + ".png").convert_alpha()
           for i in range(1, 7)]
DUCK_IMG = [pygame.image.load("data/images/dino/duck_anim/duck_anim" + str(i) + ".png").convert_alpha()
            for i in range(1, 7)]
JUMP_IMG = pygame.image.load(
    "data/images/dino/jump/dino_jump.png").convert_alpha()
DIE_IMG = pygame.image.load("data/images/dino/dino_die.png").convert_alpha()

ICON_IMG = pygame.image.load("data/images/dino/icon.png").convert_alpha()
RESTART_IMG = pygame.image.load("data/images/restart.png").convert_alpha()

CLOUD_IMG = [pygame.image.load("data/images/background/clouds/cloud_00" + f"{i:02d}" + ".png").convert_alpha()
             for i in range(0, 10)]

DESERT_IMG = [pygame.image.load("data/images/background/desert/desert_00" + f"{i:02d}" + ".png").convert_alpha()
              for i in range(0, 4)]
