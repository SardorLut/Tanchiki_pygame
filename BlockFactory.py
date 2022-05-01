from abc import ABC, abstractmethod
from random import randint

import pygame

from Boom import Boom
from Globals import Globals
from Images import Images


class Block(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass


class BrickWall(Block):
    def __init__(self, x, y, size_x, size_y):
        Globals.brick_walls.append(self)
        self.x, self.y = x, y
        self.size_x, self.size_y = size_x, size_y
        self.rect = pygame.Rect(x, y, size_x - 3, size_y - 3)

    def draw(self):
        if self.size_x == 32 and self.size_y == 32:
            wall = pygame.transform.scale(Images.WALL_IMAGE[0], (self.size_x, self.size_y))
        elif self.size_x == 64 and self.size_y == 32:
            wall = pygame.transform.scale(Images.WALL_IMAGE[1], (self.size_x, self.size_y))
        else:
            wall = pygame.transform.scale(Images.WALL_IMAGE[2], (self.size_x, self.size_y))
        Globals.window.blit(wall, (self.x, self.y))

    def update(self):  # взрыв при попадании пули
        for bullet in Globals.bullets:
            if self.rect.colliderect(bullet.rect):
                Globals.brick_walls.remove(self)
                Boom(self.rect.centerx, self.rect.centery)
                Globals.bullets.remove(bullet.rect)


class IronWall(Block):
    def __init__(self, x, y):
        Globals.iron_blocks.append(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE / 2)

    def draw(self):
        iron_block = pygame.transform.scale(Images.IRON_BLOCK_IMAGE, (Globals.TANK_SIZE, Globals.TANK_SIZE / 2))
        Globals.window.blit(iron_block, (self.x, self.y))

    def update(self):  # взрыв при попадании пули
        for bullet in Globals.bullets:
            if self.rect.colliderect(bullet.rect):
                Boom(self.rect.centerx, self.rect.centery)
                Globals.bullets.remove(bullet.rect)


class Water(Block):
    def __init__(self, x, y):
        Globals.waters.append(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)

    def draw(self):
        n = randint(0, 1)
        if n:
            watter = pygame.transform.scale(Images.WATER_IMAGE[1], (Globals.TANK_SIZE, Globals.TANK_SIZE))
        else:
            watter = pygame.transform.scale(Images.WATER_IMAGE[0], (Globals.TANK_SIZE, Globals.TANK_SIZE))
        Globals.window.blit(watter, (self.x, self.y))

    def update(self):
        pass


class BlockFactory:
    @staticmethod
    def get_block(type_of_block, x, y, size_x=None, size_y=None):
        if type_of_block == "brick":
            BrickWall(x, y, size_x, size_y)
        if type_of_block == "iron":
            IronWall(x, y)
        if type_of_block == 'water':
            Water(x, y)
