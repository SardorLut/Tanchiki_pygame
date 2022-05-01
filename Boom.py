import pygame
from Globals import Globals
from Images import Images


class Boom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.delay = 0
        self.size_of_boom = 16
        Globals.booms.append(self)
        self.FPS = Globals.FPS * 0.5

    def draw(self):
        if self.delay != self.FPS:
            if self.delay < self.FPS / 6:
                boom = pygame.transform.scale(Images.BOOMS_IMAGE[0], (self.size_of_boom, self.size_of_boom))
            elif (self.FPS / 6) < self.delay < (self.FPS / 3):
                boom = pygame.transform.scale(Images.BOOMS_IMAGE[1], (self.size_of_boom, self.size_of_boom))
            elif (self.FPS / 3) < self.delay < (self.FPS / 2):
                boom = pygame.transform.scale(Images.BOOMS_IMAGE[2], (self.size_of_boom, self.size_of_boom))
            elif (self.FPS / 2) < self.delay < (self.FPS * 5 / 6):
                boom = pygame.transform.scale(Images.BOOMS_IMAGE[3], (self.size_of_boom, self.size_of_boom))
            else:
                boom = pygame.transform.scale(Images.BOOMS_IMAGE[4], (self.size_of_boom, self.size_of_boom))
            boom.set_colorkey((0, 0, 0))
            Globals.window.blit(boom, (self.x - 24, self.y - 24))
            self.size_of_boom += 3.8
            self.delay += 1
        else:
            Globals.booms.remove(self)
