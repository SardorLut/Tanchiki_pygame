from Globals import Globals
import pygame
from Images import Images


class Panel:
    """
    Блок панели, фиксирует границы
    """
    def __init__(self, x, y):
        Globals.panels.append(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, 32, 32)

    def draw(self):
        panel = pygame.transform.scale(Images.PANEL_IMAGE, (32, 32))
        Globals.window.blit(panel, (self.x, self.y))

    def update(self):
        self.__bullet_hit_panel()

    def __bullet_hit_panel(self):
        for bullet in Globals.bullets:
            if self.rect.colliderect(bullet.rect):
                Globals.bullets.remove(bullet.rect)
