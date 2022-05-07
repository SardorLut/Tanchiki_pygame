import pygame

from Boom import Boom
from Globals import Globals
from Images import Images
import Enemy


class Bullet:
    """
    Создает пулю, двигает и отрисовывает на экране
    """

    def __init__(self, parent, x, y, v_x, v_y, direct, bullet_vel, mode):
        self.Enemy = Enemy
        Globals.bullets.append(self)
        self.mode = mode
        self.parent = parent
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, 10, 12)
        self.direct = direct
        self.bul_velocity = bullet_vel
        self.v_x, self.v_y = v_x, v_y

    def __hitting_rect_tank(self):  # взрывать танки при попадании пули
        if self.mode == "coop":
            for tank in Globals.tanks:
                if tank != self.parent and tank.rect.collidepoint(self.rect.x, self.rect.y):
                    if self in Globals.bullets:
                        Globals.bullets.remove(self)
                    if self.parent in Globals.Russiantanks or self.parent in Globals.soviettanks \
                            or self.parent in Globals.imperiantanks:
                        tank.damage()
                        Boom(self.rect.x, self.rect.y)
        else:
            for tank in Globals.tanks:
                if tank != self.parent and tank.rect.collidepoint(self.rect.x, self.rect.y):
                    if self in Globals.bullets:
                        Globals.bullets.remove(self)
                    tank.damage()
                    Boom(self.rect.x, self.rect.y)
        for russiantank in Globals.Russiantanks:
            if russiantank.rect.collidepoint(self.rect.x, self.rect.y):
                if self in Globals.bullets:
                    Globals.bullets.remove(self)
                if self.parent in Globals.tanks:
                    Globals.Russiantanks.remove(russiantank)
                    self.Enemy.Enemy(self.parent)
                    Boom(self.rect.x, self.rect.y)
        for soviettank in Globals.soviettanks:
            if soviettank.rect.collidepoint(self.rect.x, self.rect.y):
                if self in Globals.bullets:
                    Globals.bullets.remove(self)
                if self.parent in Globals.tanks:
                    soviettank.damage()
                    Boom(self.rect.x, self.rect.y)

        for imperiantank in Globals.imperiantanks:
            if imperiantank.rect.collidepoint(self.rect.x, self.rect.y):
                if self in Globals.bullets:
                    Globals.bullets.remove(self)
                if self.parent in Globals.tanks:
                    Globals.imperiantanks.remove(imperiantank)
                    self.Enemy.Enemy(self.parent)
                    Boom(self.rect.x, self.rect.y)

    def __hitting_rect_bullet(self):  # удалять пули при взаимном попадании
        for bullet in Globals.bullets:
            if bullet != self and self.rect.colliderect(bullet.rect):
                Globals.bullets.remove(bullet.rect)
                if self in Globals.bullets:
                    Globals.bullets.remove(self)

    def movement(self):
        self.rect.x += self.v_x * self.bul_velocity
        self.rect.y += self.v_y * self.bul_velocity
        self.__hitting_rect_tank()
        self.__hitting_rect_bullet()

    def draw(self):
        bullet = pygame.transform.rotate(pygame.transform.scale(Images.BULLET_IMAGE, (10, 12)), self.direct)
        Globals.window.blit(bullet, (self.rect.x, self.rect.y))
