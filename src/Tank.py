import pygame

from src.Bullet import Bullet
from src.Globals import Globals
from src.Images import Images
import src.Func


class __Hitting:
    """
    Отслеживает столкновение танка с объектами
    """

    def __init__(self):
        self.direct = None
        self.rect = None

    def _direction_of_the_shoot(self):
        # право
        if self.direct == -90:
            x = self.rect.x + self.rect.width
            y = self.rect.y + self.rect.height // 2
            return [1, 0, x, y]
            # вверх
        if self.direct == 0:
            x = self.rect.x + self.rect.width // 2
            y = self.rect.y
            return [0, -1, x, y]
            # лево
        if self.direct == 90:
            x = self.rect.x
            y = self.rect.y + self.rect.height // 2
            return [-1, 0, x, y]
            # вниз
        if self.direct == 180:
            x = self.rect.x + self.rect.width // 2
            y = self.rect.y + self.rect.height
            return [0, 1, x, y]

    def _tank_hit_iron_wall(self, x, y):  # если танк столкнулся со стеной он должен стоять
        for iron_wall in Globals.iron_blocks:
            if self.rect.colliderect(iron_wall.rect):
                self.rect.topleft = x, y

    def _tank_hit_rebirth_star(self):  # если танк столкнулся со звездой он должен стоять
        for rebirth_star in Globals.rebirth_stars:
            if self.rect.colliderect(rebirth_star.rect):
                Globals.rebirth_stars.remove(rebirth_star)

    def _tank_hit_brick_wall(self, x, y):  # если танк столкнулся со стеной он должен стоять
        for brick_wall in Globals.brick_walls:
            if self.rect.colliderect(brick_wall.rect):
                self.rect.topleft = x, y

    def _tank_hit_panel(self, x, y):  # если танк столкнулся со стеной он должен стоять
        for panel in Globals.panels:
            if self.rect.colliderect(panel.rect):
                self.rect.topleft = x, y

    def _tank_hit_water(self, x, y):  # если танк столкнулся со стеной он должен стоять
        for water in Globals.waters:
            if self.rect.colliderect(water.rect):
                self.rect.topleft = x, y

    def _hitting_tank(self, x, y):  # если два танка столкнулись они должны стоять
        for imperiantank in Globals.imperiantanks:
            if self.rect.colliderect(imperiantank.rect):
                self.rect.topleft = x, y
        for russiantank in Globals.Russiantanks:
            if self.rect.colliderect(russiantank.rect):
                self.rect.topleft = x, y
        for soviettank in Globals.soviettanks:
            if self.rect.colliderect(soviettank.rect):
                self.rect.topleft = x, y
        for tank in Globals.tanks:
            if tank != self and self.rect.colliderect(tank.rect):
                self.rect.topleft = x, y


class Tank(__Hitting):
    """
    Создает танк, инициализирует управление, стрельбу и отрисовку на экране
    """

    def __init__(self, x, y, velocity, direct, colour, keys, mode):
        super().__init__()
        self.Func = src.Func
        self.mode = mode
        self.delay = 0
        self.colour = colour
        self.x = x
        self.y = y
        self.velocity = velocity
        self.direct = direct
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE - 10, Globals.TANK_SIZE - 10)
        self.rect_hp = pygame.Rect(x, y, 30, 27)
        self.key_LEFT = keys[0]
        self.key_UP = keys[1]
        self.key_DOWN = keys[2]
        self.key_RIGHT = keys[3]
        self.key_SHOOT = keys[4]
        Globals.tanks.append(self)
        self.d = 0
        self.hp = 3

    def movement(self, keys_pressed):
        old_x, old_y = self.rect.topleft
        if keys_pressed[self.key_LEFT]:
            self.rect.x -= self.velocity
            self.direct = 90  # 1 = лево
        elif keys_pressed[self.key_RIGHT]:
            self.rect.x += self.velocity
            self.direct = -90  # 4 = право
        elif keys_pressed[self.key_UP]:
            self.rect.y -= self.velocity
            self.direct = 0
        elif keys_pressed[self.key_DOWN]:
            self.rect.y += self.velocity
            self.direct = 180  # 2 = вниз
        self._hitting_tank(old_x, old_y)
        self._tank_hit_brick_wall(old_x, old_y)
        self._tank_hit_iron_wall(old_x, old_y)
        self._tank_hit_panel(old_x, old_y)
        self._tank_hit_rebirth_star()
        self._tank_hit_water(old_x, old_y)
        if keys_pressed[self.key_SHOOT] and self.delay == Globals.FPS - 10:
            dx, dy, x_dir, y_dir = self._direction_of_the_shoot()
            Bullet(self, x_dir, y_dir, dx, dy, self.direct, Globals.BULLET_VELOCITY, self.mode)
            self.delay = 0  # скорость пули
        if self.delay != Globals.FPS - 10:
            self.delay += 1
    def draw(self):

        # менять размер и направление
        if self.colour == "yellow":
            TANK_IMAGE = pygame.transform.rotate(pygame.transform.scale
                                                 (Images.TANKS_IMAGE[0], (Globals.TANK_SIZE - 10, Globals.TANK_SIZE - 10)),
                                                 self.direct)
        else:
            TANK_IMAGE = pygame.transform.rotate(pygame.transform.scale
                                                 (Images.TANKS_IMAGE[1], (Globals.TANK_SIZE - 10, Globals.TANK_SIZE - 10)),
                                                 self.direct)
        TANK_IMAGE.set_colorkey((0, 0, 0))
        Globals.window.blit(TANK_IMAGE, (self.rect.x, self.rect.y))
    def damage(self):
        self.hp -= 1
        if self.hp == 0 and len(Globals.tanks) == 1:
            self.Func.score_menu(0, "coop")
        if self.hp == 0 and len(Globals.tanks) == 2:
            if self.mode == "coop":
                Globals.tanks.remove(self)
            if self.mode == "vs_mode" and self.colour == "white":
                self.Func.score_menu(1, "vs_mode")
            if self.mode == "vs_mode" and self.colour == "yellow":
                self.Func.score_menu(0, "vs_mode")
