from random import randint

import pygame

from Globals import Globals
from Images import Images
from TankBotFactory import TankBotFactory


class RebirthStar:
    def __init__(self, x, y):
        Globals.rebirth_stars.append(self)
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)
        self.delay = 0
        self.size = 1
        self.rem = 0
        self.x, self.y = x, y

    def draw(self):
        if self.delay != Globals.FPS:
            self.delay += 1
            self.size += 2
            if self.delay < 15:
                REBIRTH_1 = pygame.transform.scale(Images.REBIRTH_1_IMAGE, (self.size, self.size))
                Globals.window.blit(REBIRTH_1, (self.rect.x, self.rect.y))
            elif 15 <= self.delay < 30:
                REBIRTH_2 = pygame.transform.scale(Images.REBIRTH_2_IMAGE, (self.size, self.size))
                Globals.window.blit(REBIRTH_2, (self.rect.x, self.rect.y))
            elif 30 <= self.delay < 45:
                REBIRTH_3 = pygame.transform.scale(Images.REBIRTH_3_IMAGE, (self.size, self.size))
                Globals.window.blit(REBIRTH_3, (self.rect.x, self.rect.y))
            else:
                REBIRTH_4 = pygame.transform.scale(Images.REBIRTH_4_IMAGE, (self.size, self.size))
                Globals.window.blit(REBIRTH_4, (self.rect.x, self.rect.y))
        else:
            factory = TankBotFactory()
            n = randint(0, 2)
            if n == 1:
                factory.get_tank('russian', self.x, self.y, 5)
            elif n == 0:
                factory.get_tank('soviet', self.x, self.y, 5)
            else:
                factory.get_tank('imperian', self.x, self.y, 5)
            Globals.rebirth_stars.remove(self)
