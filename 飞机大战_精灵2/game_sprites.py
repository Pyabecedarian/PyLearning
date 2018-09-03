from random import choice
from pygame.sprite import Sprite
from settings import *


class GameSprite(Sprite):
    """游戏精灵"""

    def __init__(self, img_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.is_hit = False

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """背景类"""
    def __init__(self, settings, is_alt=False):
        super().__init__(settings.bg_img_path)
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机类"""
    def __init__(self, img_path, speed, armed=False):
        super().__init__(img_path)
        self.speed = speed
        self.rect.x = randint(0, Settings.SCREEN_WIDTH - self.rect.width)
        self.rect.bottom = 0
        self.armed = armed

    def update(self):
        super().update()
        if self.rect.y >= Settings.SCREEN_HEIGHT or self.is_hit:
            self.kill()

    def fire(self, settings, enemy_bullet_group):
        """开火"""
        for i in range(3):
            bullet = EnemyBullet(self, *settings.enemy_bullet_img_path[i], speed=4)
            enemy_bullet_group.add(bullet)


class Hero(GameSprite):
    """友军类"""
    def __init__(self, settings):
        super().__init__(settings.hero_img_path)
        self.rect.centerx = Settings.SCREEN_WIDTH / 2
        self.rect.bottom = Settings.SCREEN_HEIGHT - 100
        self.bullet_group = pygame.sprite.Group()
        self.missile_group = pygame.sprite.Group()
        self.hp = settings.hero_hp_limit

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= Settings.SCREEN_WIDTH:
            self.rect.right = Settings.SCREEN_WIDTH

        for bullet in self.bullet_group:
            if bullet.rect.y <= 0:
                bullet.kill()

        if self.is_hit:
            self.is_hit = False
            self.hp -= 1
            if self.hp <= 0:
                print("HP耗尽, 游戏结束")
                pygame.quit()
                exit()

    def fire(self, img_path):
        """开火"""
        bullet = Bullet(img_path, self)
        self.bullet_group.add(bullet)

    def launch(self, settings):
        """发射导弹"""
        if len(self.missile_group) < settings.missile_limit:
            missile = Missile(settings.missile_img_path, self, is_left=choice([True, False]))
            self.missile_group.add(missile)


class Bullet(GameSprite):
    """子弹类"""
    def __init__(self, img_path, hero, speed=-8):
        super().__init__(img_path)
        self.rect.centerx = hero.rect.centerx
        self.rect.bottom = hero.rect.top
        self.speed = speed

    def update(self):
        super().update()
        if self.is_hit:
            self.kill()


class Missile(GameSprite):
    """导弹类"""
    def __init__(self, img_path,  hero, speed=-0, is_left=True):
        super().__init__(img_path)
        self.speed = speed
        self.is_left = is_left
        self.clock = pygame.time.Clock()
        self.rect.centery = hero.rect.centery
        self.rect.centerx = hero.rect.centerx
        self.t = 1
        if self.is_left:
            self.origin = Settings.SCREEN_WIDTH/2 + 50
            self.speed_x = -5
        else:
            self.origin = Settings.SCREEN_WIDTH/2 - 50
            self.speed_x = 5

    def __centx(self):
        """ """
        self.position = self.rect.centerx - self.origin
        self.acc = - int(Settings.CO_K * self.position)
        self.speed_x += self.acc * self.t
        self.rect.x += self.speed_x
        self.speed -= 0.1 * self.t

        # print("左: {}, 位移: {}, 加速度: {}, 速度x:{}, 时间:{}".format(self.is_left,
        # self.position, self.acc, self.speed_x, self.t))

    def update(self):
        super().update()
        self.__centx()
        if self.rect.bottom <= 0 or self.is_hit:
            self.kill()
            # print("导弹被删")


class EnemyBullet(Bullet):
    def __init__(self,  enemy, img_path, is_down=False, is_left=False, speed=4):
        super().__init__(img_path, enemy, speed)
        self.is_down = is_down
        self.is_left = is_left
        self.rect.top = enemy.rect.bottom
        if self.is_down is True and self.is_left is False:
            self.rect.centerx = enemy.rect.centerx
        elif self.is_down is False and self.is_left is False:
            self.rect.left = enemy.rect.right
        else:
            self.rect.right = enemy.rect.left

    def update(self):
        super().update()

        if self.is_left:
            self.rect.x -= self.speed
        elif self.is_down:
            pass
        else:
            self.rect.x += self.speed

        if self.is_hit or self.rect.y >= Settings.SCREEN_HEIGHT:
            self.kill()
