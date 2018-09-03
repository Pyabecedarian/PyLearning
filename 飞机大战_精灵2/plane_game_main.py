from pygame.locals import *
from game_sprites import *


class PlaneGame:
    """主程序类"""

    def __init__(self):
        pygame.init()
        # 初始化游戏设置
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(Settings.ENEMY_CREATE_EVENT, 350)
        pygame.time.set_timer(Settings.FIRE_BULLET, 400)
        pygame.time.set_timer(Settings.MISSILE_LAUNCH, 500)
        pygame.time.set_timer(Settings.MISSILE_L_TIME, 100)
        pygame.time.set_timer(Settings.ENEMY_FIRE, 2000)
        self.game_ico = pygame.image.load("./res/app.ico")

        # 加载音乐
        pygame.mixer.music.load(self.settings.music_path)
        self.gameover_sound = pygame.mixer.Sound("./res/gameover.wav")
        # 循环播放音乐
        # pygame.mixer.music.play(-1)

        # 创建窗口
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_caption("飞机大战")

        # 创建文字对象
        self.score_font = pygame.font.Font("res/SIMHEI.TTF", 40)
        self.score = 0

    def __create_sprite(self):
        """创建精灵"""

        # 背景精灵
        self.bg1 = Background(self.settings)
        self.bg2 = Background(self.settings, True)
        self.bg_group = pygame.sprite.Group(self.bg1, self.bg2)

        # 敌军精灵
        self.enemy_group = pygame.sprite.Group()

        # 创建友军精灵
        self.hero = Hero(self.settings)
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建敌军子弹精灵
        self.enemy_bullet_group = pygame.sprite.Group()

    def __event_handler(self):
        """事件循环"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.__game_over()

            elif event.type == Settings.ENEMY_CREATE_EVENT:
                enemy = Enemy(*self.settings.enemy_img_path_dict[randint(1, 4)])
                self.enemy_group.add(enemy)

            elif event.type == Settings.FIRE_BULLET:
                self.hero.fire(self.settings.bullet_img_path)

            elif event.type == Settings.MISSILE_LAUNCH:
                self.hero.launch(self.settings)

            elif event.type == Settings.MISSILE_L_TIME:
                for missile in self.hero.missile_group:
                    missile.t += 1
            elif event.type == Settings.ENEMY_FIRE:
                for enemy in self.enemy_group:
                    if enemy.armed:
                        enemy.fire(self.settings, self.enemy_bullet_group)

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            self.hero.speed = -3
        elif pressed_key[K_RIGHT]:
            self.hero.speed = 3
        else:
            self.hero.speed = 0

    def __update_sprite(self):
        """更新精灵"""
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.enemy_bullet_group.update()
        self.enemy_bullet_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

        self.hero.missile_group.update()
        self.hero.missile_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        score_text = self.score_font.render("得分:%d" % self.score, 1, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        pygame.display.update()

    def __check_collide(self):
        """碰撞检测"""
        for enemy in self.enemy_group:
            if pygame.Rect.colliderect(enemy.rect, self.hero.rect):
                enemy.is_hit = True
                self.hero.is_hit = True
                self.score += 10
                continue
            for missile in self.hero.missile_group:
                if pygame.Rect.colliderect(missile.rect, enemy.rect):
                    missile.is_hit = True
                    enemy.is_hit = True
                    continue

            for bullet in self.hero.bullet_group:
                if pygame.Rect.colliderect(bullet.rect, enemy.rect):
                    enemy.is_hit = True
                    bullet.is_hit = True
                    self.score += 10
                    break

        for bullet in self.enemy_bullet_group:
            if pygame.Rect.colliderect(bullet.rect, self.hero.rect):
                bullet.is_hit = True
                self.hero.is_hit = True

    @staticmethod
    def __game_over():
        """游戏结束"""
        print("游戏结束")
        pygame.quit()
        exit()

    def start_game(self):
        """游戏开始"""
        pygame.display.set_icon(self.game_ico)
        print("游戏开始")
        self.__create_sprite()

        while True:
            self.clock.tick(Settings.FRAME_PER_SEC)
            self.__event_handler()
            self.__update_sprite()
            self.__check_collide()


if __name__ == '__main__':
    plane_game = PlaneGame()
    plane_game.start_game()
