import pygame

from Globals import Globals
from Images import Images


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
    """
    Вражеская база, при попадании в нее игра должна заканчиваться
    """
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)

    def update(self):
        from Func import score_menu
        for bullet in Globals.bullets:
            if self.rect.colliderect(bullet.rect):
                score_menu(0)

    def draw(self):
        baza = pygame.transform.scale(Images.BAZA_IMAGE, (Globals.TANK_SIZE, Globals.TANK_SIZE))
        Globals.window.blit(baza, (self.rect.x, self.rect.y))
