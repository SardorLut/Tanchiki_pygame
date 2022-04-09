import pygame

from Globals import Globals
from Images import Images


class Enemy:
    def __init__(self, parent):
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
        from Func import score, score_menu
        if len(Globals.enemies) == 0:
            Enemy(1)
        if self.parent in Globals.Russiantanks:
            score(100)
        elif self.parent in Globals.soviettanks:
            score(200)
        else:
            score(400)
        if 17 - len(Globals.enemies) == 0:
            if self.delay != Globals.FPS * 0.6:
                self.delay += 1
            else:
                score_menu(1)
