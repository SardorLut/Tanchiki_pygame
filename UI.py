import pygame

from Globals import Globals
from Images import Images


class UI:
    """
    Рисует на экране здоровье игрока
    """
    @staticmethod
    def draw():
        tank_hp = pygame.transform.scale(Images.PLAYER_LIFE_IMAGE, (27, 23))
        player_1 = pygame.transform.scale(Images.PLAYER_1_IMAGE, (40, 33))
        player_2 = pygame.transform.scale(Images.PLAYER_2_IMAGE, (40, 33))
        for tank in Globals.tanks:
            if tank.colour == 'yellow':
                Globals.window.blit(player_1, (Globals.WIDTH - 66, 370))
                for i in range(tank.hp):
                    Globals.window.blit(tank_hp, (Globals.WIDTH - 90 + 30 * i, 410))
            if tank.colour == 'white':
                Globals.window.blit(player_2, (Globals.WIDTH - 66, 450))
                for i in range(tank.hp):
                    Globals.window.blit(tank_hp, (Globals.WIDTH - 90 + 30 * i, 490))
