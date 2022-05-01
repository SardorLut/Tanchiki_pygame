import pygame
from Globals import Globals
from Images import Images
import Func


class Enemy:
    def __init__(self, parent):
        self.Func = Func
        self.parent = parent
        self.delay = 0
        Globals.enemies.append(self)
        self.rect = []
        for i in range(8):
            for j in range(2):
                self.rect.append(pygame.Rect(Globals.WIDTH - 80 + 30 * j, 40 + 30 * i, 30, 27))

    def draw(self):
        life = pygame.transform.scale(Images.LIFE_IMAGE, (30, 27))
        for i in range(17 - len(Globals.enemies)):
            Globals.window.blit(life, (self.rect[i].x, self.rect[i].y))

    def update(self):
        if 17 - len(Globals.enemies) == 0:
            if self.delay != Globals.FPS * 0.6:
                self.delay += 1
            else:
                self.Func.score_menu(1, "coop")
