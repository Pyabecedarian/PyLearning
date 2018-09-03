import pygame
from random import randint


class Settings:
    """游戏设置类"""
    SCREEN_WIDTH = 512
    SCREEN_HEIGHT = 768
    FRAME_PER_SEC = 60
    ENEMY_CREATE_EVENT = pygame.USEREVENT
    FIRE_BULLET = pygame.USEREVENT + 1
    MISSILE_LAUNCH = pygame.USEREVENT + 2
    MISSILE_L_TIME = pygame.USEREVENT + 3
    ENEMY_FIRE = pygame.USEREVENT + 4
    CO_K = 0.01

    def __init__(self):
        self.music_path = "./res/bg2.ogg"
        self.bg_img_path = "./res/img_bg_level_{}.jpg".format(randint(1, 5))
        self.hero_img_path = "./res/hero2.png"
        self.enemy_img_path_dict = {
            1: ("./res/img-plane_1.png", 2, True),
            2: ("./res/img-plane_3.png", 4, False),
            3: ("./res/img-plane_5.png", 6, False),
            4: ("./res/img-plane_7.png", 8, False),
        }
        self.bullet_img_path = "./res/bullet_9.png"
        self.missile_img_path = "./res/bullet_14.png"
        self.enemy_bullet_img_path1 = "./res/bullet_3.png"
        self.enemy_bullet_img_path2 = "./res/bullet_4.png"
        self.enemy_bullet_img_path = {
            0: [self.enemy_bullet_img_path2, False, False],
            1: [self.enemy_bullet_img_path1, True, False],
            2: [self.enemy_bullet_img_path2, True, True],
        }

        self.missile_limit = 4
        self.score = 0
        self.hero_hp_limit = 3
