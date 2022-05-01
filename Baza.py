import pygame

from Globals import Globals
from Images import Images
import Func


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Baza(metaclass=Singleton):
    def __init__(self, x, y):
        self.Func = Func
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)

    def update(self):
        for bullet in Globals.bullets:
            if self.rect.colliderect(bullet.rect):

                self.Func.score_menu(0, "coop")

    def draw(self):
        baza = pygame.transform.scale(Images.BAZA_IMAGE, (Globals.TANK_SIZE, Globals.TANK_SIZE))
        Globals.window.blit(baza, (self.rect.x, self.rect.y))
