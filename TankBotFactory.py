from abc import ABC, abstractmethod
from random import randint
from Enemy import Enemy
import pygame

from Bullet import Bullet
from Globals import Globals
from Images import Images


class TankBot(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def movement(self):
        pass


class RussianTank(TankBot):
    def __init__(self, x, y, velocity):
        Globals.total += 1
        Globals.Russiantanks.append(self)
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE - 4, Globals.TANK_SIZE - 4)
        self.velocity = velocity - 2
        self.direct = 0
        self.d = 0
        self.delay = 0
        self.bul_velocity = 0

    def __direction_of_the_shoot(self):  # направление выстрела
        # право
        if self.direct * 90 == 270:
            x = self.rect.x + self.rect.width
            y = self.rect.y + self.rect.height // 2
            return [1, 0, x, y]
            # вверх
        if self.direct * 90 == 0:
            x = self.rect.x + self.rect.width // 2
            y = self.rect.y
            return [0, -1, x, y]
            # лево
        if self.direct * 90 == 90:
            x = self.rect.x
            y = self.rect.y + self.rect.height // 2
            return [-1, 0, x, y]
            # вниз
        if self.direct * 90 == 180:
            x = self.rect.x + self.rect.width // 2
            y = self.rect.y + self.rect.height
            return [0, 1, x, y]

    def __tank_hit_rebirth_star(self):  # если танк столкнулся со звездой он должен стоять
        for rebirth_star in Globals.rebirth_stars:
            if self.rect.colliderect(rebirth_star.rect):
                Globals.rebirth_stars.remove(rebirth_star)

    def __tank_hit_iron_wall(self, x, y):  # если танк столкнулся со стеной он должен стоять
        for iron_wall in Globals.iron_blocks:
            if self.rect.colliderect(iron_wall.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)

    def __tank_hit_brick_wall(self, x, y):  # если танк столкнулся со стеной он должен стоять
        for brick_wall in Globals.brick_walls:
            if self.rect.colliderect(brick_wall.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)

    def __tank_hit_panel(self, x, y):  # если танк столкнулся со панелью он должен стоять
        for panel in Globals.panels:
            if self.rect.colliderect(panel.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)

    def __tank_hit_water(self, x, y):  # если танк столкнулся со стеной он должен стоять
        for water in Globals.waters:
            if self.rect.colliderect(water.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)

    def __hitting_tank(self, x, y):  # если два танка столкнулись они должны стоять
        for tank in Globals.tanks:
            if self.rect.colliderect(tank.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)
        for Russiantank in Globals.Russiantanks:
            if Russiantank != self and self.rect.colliderect(Russiantank.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)
        for soviettank in Globals.soviettanks:
            if soviettank != self and self.rect.colliderect(soviettank.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)
        for imperiantank in Globals.imperiantanks:
            if imperiantank != self and self.rect.colliderect(imperiantank.rect):
                self.rect.topleft = x, y
                self.d = randint(0, 3)

    def movement(self):
        old_x, old_y = self.rect.topleft
        self.direct = self.d
        if self.direct == 1:  # лево
            self.rect.x -= self.velocity
        elif self.direct == 2:  # вниз
            self.rect.y += self.velocity
        elif self.direct == 0:  # вверх
            self.rect.y -= self.velocity
        elif self.direct == 3:  # право
            self.rect.x += self.velocity
        self.__hitting_tank(old_x, old_y)  # если два танка столкнулись они должны стоять
        self.__tank_hit_brick_wall(old_x, old_y)
        self.__tank_hit_iron_wall(old_x, old_y)
        self.__tank_hit_panel(old_x, old_y)
        self.__tank_hit_rebirth_star()
        self.__tank_hit_water(old_x, old_y)
        if self.delay == Globals.FPS - 10:
            dx, dy, x_dir, y_dir = self.__direction_of_the_shoot()
            Bullet(self, x_dir, y_dir, dx, dy, self.direct * 90, Globals.BULLET_VELOCITY + self.bul_velocity, "coop")
            self.delay = 0
        else:
            self.delay += 1

    def draw(self):
        n = randint(0, 1)
        if n:
            TANK = pygame.transform.rotate(pygame.transform.scale
                                           (Images.TANKS_IMAGE[2], (Globals.TANK_SIZE, Globals.TANK_SIZE)),
                                           self.direct * 90)
        else:
            TANK = pygame.transform.rotate(pygame.transform.scale
                                           (Images.TANKS_IMAGE[5], (Globals.TANK_SIZE, Globals.TANK_SIZE)),
                                           self.direct * 90)
        Globals.window.blit(TANK, (self.rect.x, self.rect.y))


class SovietTank(RussianTank):
    def __init__(self, x, y, velocity):
        Globals.total += 1
        Globals.soviettanks.append(self)
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)
        self.velocity = velocity * 0.5
        self.direct = 0
        self.d = 0
        self.delay = 0
        self.bul_velocity = 2
        self.pause = 0
        self.hp = 3
    def draw(self):
        n = randint(0, 1)
        if n:
            TANK = pygame.transform.rotate(pygame.transform.scale
                                           (Images.TANKS_IMAGE[3], (Globals.TANK_SIZE, Globals.TANK_SIZE + 6)),
                                           self.direct * 90)
        else:
            TANK = pygame.transform.rotate(pygame.transform.scale
                                           (Images.TANKS_IMAGE[6], (Globals.TANK_SIZE, Globals.TANK_SIZE + 6)),
                                           self.direct * 90)
        Globals.window.blit(TANK, (self.rect.x, self.rect.y))
    def damage(self):
        self.hp -= 1
        if self.hp == 0:
            Enemy(self)
            Globals.soviettanks.remove(self)
class ImperianTank(RussianTank):
    def __init__(self, x, y, velocity):
        Globals.total += 1
        Globals.imperiantanks.append(self)
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)
        self.velocity = velocity * 1.5
        self.direct = 0
        self.d = 0
        self.delay = 0
        self.bul_velocity = 0
        self.pause = 30

    def draw(self):
        n = randint(0, 1)
        if n:
            TANK = pygame.transform.rotate(pygame.transform.scale
                                           (Images.TANKS_IMAGE[4], (Globals.TANK_SIZE, Globals.TANK_SIZE + 6)),
                                           self.direct * 90)
        else:
            TANK = pygame.transform.rotate(pygame.transform.scale
                                           (Images.TANKS_IMAGE[7], (Globals.TANK_SIZE, Globals.TANK_SIZE + 6)),
                                           self.direct * 90)
        Globals.window.blit(TANK, (self.rect.x, self.rect.y))


class TankBotFactory:
    @staticmethod
    def get_tank(type_of_tank, x, y, velocity):
        if type_of_tank == "russian":
            RussianTank(x, y, velocity)
        if type_of_tank == "soviet":
            SovietTank(x, y, velocity)
        if type_of_tank == 'imperian':
            ImperianTank(x, y, velocity)
