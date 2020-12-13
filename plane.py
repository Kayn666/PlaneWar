import pygame
import random


# changed by chenyuyang
class Hero(object):
    def __init__(self, screen):
        # 加载hero飞机界面
        self.image = pygame.image.load('images/hero.png')
        # 加载hero飞机爆炸图片
        self.images = []
        self.images.extend([
            pygame.image.load('images/hero_blowup_n1.png'),
            pygame.image.load('images/hero_blowup_n2.png'),
            pygame.image.load('images/hero_blowup_n3.png'),
            pygame.image.load('images/hero_blowup_n4.png')
        ])
        self.__x = 140
        self.__y = 450
        self.__is_double_bullet = False  # 初始状态为False，表示单发子弹,True表示双发子弹
        self.__is_speed_bullet = False  # 初始状态为False，表示普通子弹,True表示高速子弹
        self.__rect = self.image.get_rect()
        self.__speed = 4
        self.__score = 0
        self.screen = screen

    def init_position(self):
        self.__x = 140
        self.__y = 450

    def set_score(self, new_score):
        self.__score = new_score

    def get_score(self):
        return self.__score

    def up(self):
        self.__y -= self.__speed

    def down(self):
        self.__y += self.__speed

    def left(self):
        self.__x -= self.__speed

    def right(self):
        self.__x += self.__speed

    def get_x(self):
        return self.__x

    def set_x(self, change_x):
        self.__x = change_x

    def get_y(self):
        return self.__y

    def set_y(self, change_y):
        self.__y = change_y

    def get_rect(self):
        return self.__rect

    def set_rect(self, change_rect):
        self.__rect = change_rect

    def get_speed(self):
        return self.__speed

    def set_speed(self, change_speed):
        self.__speed = change_speed

    def get_double_bullet_status(self):
        return self.__is_double_bullet

    def set_double_bullet_status(self,change_status):
        self.__is_double_bullet = change_status

    def get_speed_bullet_status(self):
        return self.__is_speed_bullet

    def set_speed_bullet_status(self, change_status):
        self.__is_speed_bullet = change_status

    def draw_hero_plane(self):
        self.screen.blit(self.image, (self.__x, self.__y))


# 补给类，changed by chenyuyang
class Supply(object):
    def __init__(self, screen):
        # 补给机
        self.image = pygame.image.load("./images/bomb-1.png")
        self.rect = self.image.get_rect()  # 获得补给机宽高
        # 　随机补给机初始位置
        self.x = random.randint(120, 300 - self.rect.width)
        self.rand = random.randint(18,25)
        self.y = - 5*self.rect.height
        self.screen = screen

    def move(self):
        if self.y < 700:
            self.y += 1
        else:
            self.x = random.randint(0, 500 - self.rect.width)
            self.y = - self.rect.height

    def draw(self):
        self.move()
        # 绘制 补给机
        self.screen.blit(self.image, (self.x, self.y))

    def reset(self):
        # 补给机回到初始位置
        self.x = random.randint(120, 300 - self.rect.width)
        self.y = - self.rand * self.rect.height

    def collision(self, b_object):
        if self.x + self.rect.width > b_object.get_x() and \
                self.x < b_object.get_x() + b_object.get_rect().width and \
                self.y < b_object.get_y() + b_object.get_rect().height and \
                self.y + self.rect.height > b_object.get_y() :
            return True
        else:
            return False


# 补给类，changed by chenyuyang
class BulletSpeedUp(object):
    def __init__(self, screen):
        # 补给机
        self.image = pygame.image.load("./images/bomb-2.png")
        self.rect = self.image.get_rect()  # 获得补给机宽高
        # 　随机补给机初始位置
        self.x = random.randint(120, 300 - self.rect.width)
        self.rand = random.randint(10, 15)
        self.y = - 2*self.rect.height
        self.screen = screen

    def move(self):
        if self.y < 700:
            self.y += 1
        else:
            self.x = random.randint(0, 500 - self.rect.width)
            self.y = - self.rect.height

    def draw(self):
        self.move()
        # 绘制 补给机
        self.screen.blit(self.image, (self.x, self.y))

    def reset(self):
        # 补给机回到初始位置
        self.x = random.randint(120, 300 - self.rect.width)
        self.y = - self.rand*self.rect.height

    def collision(self, b_object):
        if self.x + self.rect.width > b_object.get_x() and \
                self.x < b_object.get_x() + b_object.get_rect().width and \
                self.y < b_object.get_y() + b_object.get_rect().height and \
                self.y + self.rect.height > b_object.get_y() :
            return True
        else:
            return False


class Bullet:

    def __init__(self, screen, hero, state=1):
        # 当state为1的时候是主机，当state为0的时候是敌机
        if state == 1:
            self.__image = pygame.image.load('images/bullet1.png')
        elif state == 0:
            self.__image = pygame.image.load('images/enemy_bullet.png')
        self.screen = screen
        self.__bullet_rect = self.__image.get_rect()
        self.__bx = hero.get_x() + hero.get_rect().width / 2 - self.__bullet_rect.width / 2 + 1
        if state == 1:
            self.__by = hero.get_y() - self.__bullet_rect.height
            self.__bullet_speed = 20
        elif state == 0:
            self.__bullet_speed = 7
            self.__by = hero.get_y() + self.__bullet_rect.height+30

        self.__double_bx1 = self.__bx + 15
        self.__double_bx2 = self.__bx - 15

    def set_bx(self,new_bx):
        self.__bx=new_bx

    def set_by(self,new_by):
        self.__by=new_by

    def get_bx(self):
        return  self.__bx

    def get_by(self):
        return  self.__by

    def set_bullet_speed(self,new_bullet_speed):
        self.__bullet_speed=new_bullet_speed

    def get_speed(self):
        return  self.__bullet_speed

    def get_rect(self):
        return  self.__bullet_rect

    def bullet_move(self,hero):
        if self.__by >= -self.__bullet_rect.height:
            self.__by-=self.__bullet_speed
        else:
            self.__bx = hero.get_x() + hero.get_rect().width / 2 - self.__bullet_rect.width / 2 + 1
            self.__by = hero.get_y() - self.__bullet_rect.height

    def draw_bullet(self):
        self.screen.blit(self.__image,(self.__bx,self.__by))

    def draw_double_bullet(self):
        self.screen.blit(self.__image, (self.__double_bx1, self.__by))
        self.screen.blit(self.__image, (self.__bx, self.__by))
        self.screen.blit(self.__image, (self.__double_bx2, self.__by))
        self.__double_bx1 = self.__bx + 55
        self.__double_bx2 = self.__bx - 55

    def single_bullet_hit_enemy(self, enemy_0, bullet, hero, xx, yy):
        if -enemy_0.get_rect().width < xx < bullet.get_rect().width \
                and -enemy_0.get_rect().height < yy < bullet.get_rect().height:  # 击中敌机
            return True
        else:
            return False

    def double_bullet_hit_enemy(self, enemy, bullet, hero, xx, yy):
        x1 = xx + 55
        x2 = xx - 55
        if self.single_bullet_hit_enemy(enemy,bullet,hero,x1,yy) or \
                self.single_bullet_hit_enemy(enemy,bullet,hero,x2,yy):
            return True
        else:
            return False

    # 敌机子弹移动
    def bullet_enemy_move(self, hero):
        if self.__by <= 600 - self.__bullet_rect.height:
            self.__by += 5
        else:
            self.__bx = hero.get_x() + hero.get_rect().width / 2 - self.__bullet_rect.width / 2 + 1
            self.__by = hero.get_y() + self.__bullet_rect.height + 30

    # 敌机击中主机检测
    def single_bullet_kill_hero(self,bullet,hero):
        if hero.get_x()-bullet.get_rect().width < bullet.get_bx() < hero.get_x()+hero.get_rect().width and \
                hero.get_y()-bullet.get_rect().height < bullet.get_by() < hero.get_y()+hero.get_rect().height:
            return True


class Enemy:
    """
    author: JinQi
    """
    SMALL = 0
    MEDIUM = 1
    BIG = 2
    __enemies = []

    def __init__(self, spc, screen):
        self.__screen = screen
        self.__speed = random.randint(1, 5) / 10 + 2.0
        self.__spc = spc
        if spc == Enemy.SMALL:
            self.__img_url = 'images/enemy0.png'
            self.__enemy_plane0_blowup1 = pygame.image.load('images/enemy0_down1.png')
            self.__enemy_plane0_blowup2 = pygame.image.load('images/enemy0_down2.png')
            self.__enemy_plane0_blowup3 = pygame.image.load('images/enemy0_down3.png')
            self.__enemy_plane0_blowup4 = pygame.image.load('images/enemy0_down4.png')
            self.__hp = 1
        elif spc == Enemy.MEDIUM:
            self.__img_url = 'images/enemy1.png'
            self.__enemy_plane0_blowup1 = pygame.image.load('images/enemy1_down1.png')
            self.__enemy_plane0_blowup2 = pygame.image.load('images/enemy1_down2.png')
            self.__enemy_plane0_blowup3 = pygame.image.load('images/enemy1_down3.png')
            self.__enemy_plane0_blowup4 = pygame.image.load('images/enemy1_down4.png')
            self.__hp = 5
        else:
            self.__img_url = 'images/enemy2.png'
            self.__enemy_plane0_blowup1 = pygame.image.load('images/enemy2_down1.png')
            self.__enemy_plane0_blowup2 = pygame.image.load('images/enemy2_down2.png')
            self.__enemy_plane0_blowup3 = pygame.image.load('images/enemy2_down3.png')
            self.__enemy_plane0_blowup4 = pygame.image.load('images/enemy2_down4.png')
            self.__hp = 10
        self.__x, self.__y = self.get_init_xy()

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp

    def get_spc(self):
        return self.__spc

    def move(self):
        self.__y += self.__speed

    def reset(self):
        if self.__spc == self.SMALL:
            self.set_hp(1)
        elif self.__spc == self.MEDIUM:
            self.set_hp(5)
        else:
            self.set_hp(10)
        self.__x = random.randint(0, 500 - self.get_rect().width)
        self.__y = -self.get_rect().height

    def get_image(self):
        return pygame.image.load(self.__img_url)

    def get_rect(self):
        return self.get_image().get_rect()

    def get_init_xy(self):  # 获取初始坐标
        return random.randint(0, 500 - self.get_rect().width), -self.get_rect().height

    def blowup(self):  # 爆炸
        ex = self.get_x()
        ey = self.get_y()
        self.__screen.blit(self.__enemy_plane0_blowup1, (ex, ey))
        pygame.display.update()
        pygame.time.delay(8)
        self.__screen.blit(self.__enemy_plane0_blowup2, (ex, ey))
        pygame.display.update()
        pygame.time.delay(8)
        self.__screen.blit(self.__enemy_plane0_blowup3, (ex, ey))
        pygame.display.update()
        pygame.time.delay(8)
        self.__screen.blit(self.__enemy_plane0_blowup4, (ex, ey))
        pygame.display.update()
        pygame.time.delay(10)
        #敌机爆炸声音
        channel1.play(enemy1_down_sound)

    def draw(self):
        screen.blit(self.get_image(), (self.get_x(), self.get_y()))

    @staticmethod
    def get_enemies():
        return Enemy.__enemies

    @staticmethod
    def add_enemies(spc):
        Enemy.__enemies.append(Enemy(spc, screen))

    @staticmethod
    def reset_enemies():
        Enemy.__enemies.clear()


class Bomb:  # 炸弹类
    def __init__(self, screen):
        self.image = pygame.image.load('./images/bomb1.png')
        self.num = 3
        self.screen = screen

    def bigBomb(self, enemies):
        for enemy in enemies:
            enemy.blowup()
            enemy.reset()

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

    def draw(self, font):
        self.screen.blit(self.image, (10, 700 - self.image.get_rect().height - 10))
        num_ = font.render('x' + str(self.num), True, (255, 255, 255))
        self.screen.blit(num_, (10 + self.image.get_rect().width, 700 - self.image.get_rect().height))


class Start(object):

    def __init__(self,screen,hero):
        self.screen = screen
        self.background = pygame.image.load('images/background.png')
        self.background_rect = self.background.get_rect()
        self.start_background = pygame.image.load('images/start.jpg')
        self.title = pygame.image.load('images/title.png')
        self.title = pygame.transform.scale(self.title,(520,200))
        self.background_y1 = - self.background_rect.height
        self.background2 = self.background
        self.background1 = self.background
        self.background_y2 = 0
        self.background_speed = 1

        # self.font = pygame.font.SysFont('C:\Windows\Fonts\Arial.ttf', 40)
        self.game_over = False
        self.game_over_flag = True
        self.menu_flag = True
        self.start_flag = False

    def draw_background(self):
        # 背景滑动开始
        self.background_y1 += self.background_speed
        if self.background_y1 >= 0:
            self.background_y1 = -self.background_rect.height
        self.background_y2 += self.background_speed
        if self.background_y2 >= self.background_rect.height:
            self.background_y2 = 0
        screen.blit(self.background2, (0, self.background_y1))
        screen.blit(self.background1, (0, self.background_y2))
        # 背景滑动结束

    def menu(self):
        screen.blit(self.start_background,(0,0))
        screen.blit(self.title,(0,0))


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption('雷电2018')
    # 英雄机实例化
    hero = Hero(screen)
    #开始界面初始化
    start = Start(screen,hero)
    # 实例化补给类
    supply1 = Supply(screen)
    # 实例化子弹加速类
    bullet_speed_up = BulletSpeedUp(screen)
    bullet = Bullet(screen, hero)
    bomb = Bomb(screen)
    font = pygame.font.Font('font\ITCKRIST.TTF', 40)

    deplay = 0

    #加载声音文件路径,初始化声音通道
    channel0 = pygame.mixer.Channel(2)
    game_bgm = pygame.mixer.Sound("sound/game_music.ogg")
    game_bgm.set_volume(0.6)
    me_down_sound = pygame.mixer.Sound("sound/me_down.wav")

    channel1 = pygame.mixer.Channel(3)
    enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")

    channel2 = pygame.mixer.Channel(4)
    enemy3_flying_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
    supply_sound = pygame.mixer.Sound("sound/bullet.wav")
    supply_sound.set_volume(0.4)
    upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
    upgrade_sound.set_volume(0.5)
    use_bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")

    while True:
        start.draw_background()
        deplay += 1
        if deplay % 5 ==0:
            hero.image = pygame.image.load('images/hero2.png')
        else:
            hero.image = pygame.image.load('images/hero.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                # 菜单界面
                if start.menu_flag:
                    if chr(event.key) == 's':  # 开始游戏
                        # 初始化
                        enemy_0 = Enemy(Enemy.SMALL, screen)
                        Enemy.reset_enemies()
                        Enemy.add_enemies(Enemy.SMALL)
                        bullet_0 = Bullet(screen, enemy_0, 0)  # 初始化敌机的子弹
                        # 初始化开始状态为True
                        start.start_flag = True
                        start.menu_flag = False
                        # 初始化hero飞机状态
                        hero.set_double_bullet_status(False)
                        hero.set_speed_bullet_status(False)
                        # 初始化hero飞机位置
                        hero.init_position()
                        # 初始化补给机的位置
                        supply1.reset()
                        bullet_speed_up.reset()
                        # 初始化hero机的速度
                        bullet.set_bullet_speed(40)
                        hero.set_speed(5)
                        start.game_over = False
                        start.game_over_flag = True
                        hero.set_score(0)
                        # 播放背景声音
                        game_bgm.play(-1)
                        #channel0.play(game_bgm)
                        bomb.set_num(3)
                    elif chr(event.key) == 'q':  # 退出游戏
                        exit()
                else:
                    if chr(event.key) == ' ':
                        bomb_num = bomb.get_num()
                        if bomb_num > 0:
                            bomb.bigBomb(Enemy.get_enemies())
                            channel1.play(use_bomb_sound)
                            bomb.set_num(bomb_num - 1)

        if start.start_flag and not start.game_over:
            # 画出补给类
            supply1.draw()
            #补给音效
            channel2.play(supply_sound)
            # 画出子弹补给类
            bullet_speed_up.draw()
            # 补给音效
            channel2.play(supply_sound)
            # 游戏运行总时间
            total_time = pygame.time.get_ticks() / 1000
            time_total = font.render("总时间:"+str(total_time), True, (255, 255, 255))

        if start.game_over:
            if start.game_over_flag:
                # 播放英雄机爆炸音效并停止背景音乐
                channel0.play(me_down_sound)
                game_bgm.stop()
                for i in range(2):
                    screen.blit(hero.images[0], (hero.get_x(), hero.get_y()))
                    pygame.display.update()
                    pygame.time.delay(100)
                    screen.blit(hero.images[1], (hero.get_x(), hero.get_y()))
                    pygame.display.update()
                    pygame.time.delay(100)
                    screen.blit(hero.images[2], (hero.get_x(), hero.get_y()))
                    pygame.display.update()
                    pygame.time.delay(100)
                    screen.blit(hero.images[3], (hero.get_x(), hero.get_y()))
                    pygame.display.update()
                    pygame.time.delay(100)
                screen.blit(hero.images[2], (hero.get_x(), hero.get_y()))
                pygame.display.update()
                pygame.time.delay(100)
                start.menu_flag = True
                start.game_over_flag = False
            else:
                screen.blit(hero.images[2], (hero.get_x(), hero.get_y()))

        if start.menu_flag:
            start.menu()
            score = hero.get_score()
            if score > 0:
                score__ = font.render('Score: ' + str(score), True, (255, 255, 255))
                screen.blit(score__, ((500 - score__.get_rect().width) / 2,
                                      (700 - score__.get_rect().height) / 2))
        else:
            keys = pygame.key.get_pressed()
            # WASD
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and hero.get_y() >= 0:
                hero.up()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and hero.get_x() >= -hero.get_rect().width // 2:
                hero.left()
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and hero.get_y() <= 700 - hero.get_rect().height:
                hero.down()
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and hero.get_x() <= 500 - hero.get_rect().width // 2:
                hero.right()
            if keys[pygame.K_SPACE]:
                pass
            hero.draw_hero_plane()
            bomb.draw(font)

            # hero机状态改变导致子弹数量的改变
            if not hero.get_double_bullet_status():
                bullet.draw_bullet()
                if start.start_flag: this_time = total_time
            else:
                bullet.draw_double_bullet()  # 显示双弹，同时在下面的碰撞检测中使用双弹检测方法
                if total_time - this_time > 10:
                    hero.set_double_bullet_status(False)

            if not hero.get_speed_bullet_status():  # 加速buff
                if start.start_flag:
                    this_time_2 = total_time
            else:
                if total_time - this_time_2 > 7:
                    bullet.set_bullet_speed(40)
                    hero.set_speed_bullet_status(False)

            bullet.bullet_move(hero)
            # 敌机随机出现
            enemies = Enemy.get_enemies()
            for enemy in enemies:
                if enemy.get_y() <= 700:
                    enemy.move()
                else:
                    enemy.reset()
                enemy.draw()
                spc = enemy.get_spc()
                if spc == Enemy.BIG or spc == Enemy.MEDIUM:
                    bullet_0.draw_bullet()  # 敌机发射单弹
                    bullet_0.bullet_enemy_move(enemy)  # 敌机子弹移动
                # 补给机碰撞检测：检测补给机是否和hero机碰撞，碰撞变双弹
                if supply1.collision(hero):
                    # 回到初始位置
                    supply1.reset()
                    # 改变hero机的状态
                    hero.set_double_bullet_status(True)
                    # 播放升级音效
                    channel1.play(upgrade_sound)
                # 子弹补给类碰撞检测
                if bullet_speed_up.collision(hero):
                    bullet_speed_up.reset()
                    hero.set_speed_bullet_status(True)
                    bullet.set_bullet_speed(150)
                    channel1.play(upgrade_sound)
                # 子弹碰撞检测
                score = hero.get_score()
                score_ = font.render(str(score), True, (255, 255, 255))
                screen.blit(score_, (20, 20))
                xx = enemy.get_x() - bullet.get_bx()
                yy = enemy.get_y() - bullet.get_by()
                if not hero.get_double_bullet_status():
                    if bullet.single_bullet_hit_enemy(enemy, bullet, hero, xx, yy):
                        bullet.set_bx(-bullet.get_rect().width)
                        bullet.set_by(-bullet.get_rect().height)
                        enemy.set_hp(enemy.get_hp() - 1)
                        if enemy.get_hp() <= 0:
                            score = hero.get_score()
                            score += 10
                            # 游戏逐渐增加难度
                            if score == 100:  # 加一个小型敌机
                                Enemy.add_enemies(Enemy.SMALL)
                            elif score == 250:  # 加一个小型敌机
                                # enemy_0 = Enemy(Enemy.SMALL, screen)
                                Enemy.add_enemies(Enemy.SMALL)
                            elif score == 400:  # 加一个中型敌机
                                # enemy_1 = Enemy(Enemy.MEDIUM, screen)
                                Enemy.add_enemies(Enemy.MEDIUM)
                            elif score == 550:  # 加一个大型敌机
                                # enemy_2 = Enemy(Enemy.BIG, screen)
                                Enemy.add_enemies(Enemy.BIG)
                            elif score == 650:
                                Enemy.add_enemies(Enemy.SMALL)
                            elif score == 800:
                                Enemy.add_enemies(Enemy.MEDIUM)
                            # print(len(enemies))
                            hero.set_score(score)
                            enemy.blowup()
                            enemy.reset()
                        bullet.set_bx(hero.get_x() + hero.get_rect().width / 2 - bullet.get_rect().width / 2 + 1)
                        bullet.set_by(hero.get_y() - bullet.get_rect().height)
                else:
                    if bullet.double_bullet_hit_enemy(enemy, bullet, hero, xx, yy):
                        bullet.set_bx(-bullet.get_rect().width)
                        bullet.set_by(-bullet.get_rect().height)
                        enemy.set_hp(enemy.get_hp() - 1)
                        if enemy.get_hp() <= 0:
                            score = hero.get_score()
                            score += 10
                            # 游戏逐渐增加难度
                            if score == 100:  # 加一个小型敌机
                                Enemy.add_enemies(Enemy.SMALL)
                            elif score == 250:  # 加一个小型敌机
                                # enemy_0 = Enemy(Enemy.SMALL, screen)
                                Enemy.add_enemies(Enemy.SMALL)
                            elif score == 400:  # 加一个中型敌机
                                # enemy_1 = Enemy(Enemy.MEDIUM, screen)
                                Enemy.add_enemies(Enemy.MEDIUM)
                            elif score == 550:  # 加一个大型敌机
                                # enemy_2 = Enemy(Enemy.BIG, screen)
                                Enemy.add_enemies(Enemy.BIG)
                            elif score == 650:
                                Enemy.add_enemies(Enemy.SMALL)
                            elif score == 800:
                                Enemy.add_enemies(Enemy.MEDIUM)
                            hero.set_score(score)
                            enemy.blowup()
                            enemy.reset()
                        bullet.set_bx(hero.get_x() + hero.get_rect().width / 2 - bullet.get_rect().width / 2 + 1)
                        bullet.set_by(hero.get_y() - bullet.get_rect().height)

                # 飞机碰撞检测
                xx = hero.get_x() - enemy.get_x()
                yy = hero.get_y() - enemy.get_y()
                if -hero.get_rect().width < xx < enemy.get_rect().width \
                        and -hero.get_rect().height < yy < enemy.get_rect().height or \
                        bullet_0.single_bullet_kill_hero(bullet_0, hero):
                    start.game_over = True
        pygame.display.update()
