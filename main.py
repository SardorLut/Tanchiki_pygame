import pygame
import os

from abc import ABC, abstractmethod

WIDTH, HEIGHT = 600, 400
pygame.display.set_caption("Танчики")
window = pygame.display.set_mode((WIDTH, HEIGHT))
#переменные
FPS = 30
VELOCITY = 5
BULLET_VELOCITY = 10
TANK_SIZE = 64
BLACK = (0, 0, 0)
#списки для штук
tanks = []
bullets = []
booms = []
#Загрузка картиночек
TANKS_IMAGE = [pygame.image.load(os.path.join('assets', 'tank_1.png')),
               pygame.image.load(os.path.join('assets', 'tank_2.png'))]
BULLET_IMAGE = pygame.image.load(os.path.join('assets', 'bullet.png'))
BOOM_IMAGE = pygame.image.load(os.path.join('assets', 'boom.png'))

def init_tanks():
    Tank(0, 0, VELOCITY, 0, 'yellow', (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_LCTRL))
    Tank(100, 100, VELOCITY, 0, 'white', (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_RCTRL))


class Builder(ABC):
    """
    Интерфейс Строителя объявляет создающие методы для различных частей объектов.
    """
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def movement(self):
        pass


class Tank(Builder):
    """
    Создает танк, инициализирует управление, стрельбу и отрисовку на экране
    """
    def __init__(self,x, y, velocity, direct, colour, keys):
        self.delay = FPS
        self.colour = colour
        self.x = x
        self.y = y
        self.velocity = velocity
        self.direct = direct
        self.rect = pygame.Rect(x, y, TANK_SIZE, TANK_SIZE)
        self.key_LEFT = keys[0]
        self.key_UP = keys[1]
        self.key_DOWN = keys[2]
        self.key_RIGHT = keys[3]
        self.key_SHOOT = keys[4]
        tanks.append(self)
    def __direction_of_the_shoot(self):
            # право
        if self.direct == -90:
            x = self.rect.x + self.rect.width
            y = self.rect.y + self.rect.height // 2
            direct_bullet = [1, 0, x, y]
            # вверх
        if self.direct == 0:
            x = self.rect.x + self.rect.width // 2
            y = self.rect.y
            direct_bullet = [0, -1, x, y]
            # лево
        if self.direct == 90:
            x = self.rect.x
            y = self.rect.y + self.rect.height // 2
            direct_bullet = [-1, 0, x, y]
            # вниз
        if self.direct == 180:
            x = self.rect.x + self.rect.width // 2
            y = self.rect.y + self.rect.height
            direct_bullet = [0, 1, x, y]
        return direct_bullet
    def movement(self, keys_pressed):
        if keys_pressed[self.key_LEFT] and self.rect.x - self.velocity > 0:
            self.rect.x -= self.velocity
            self.direct = 90
        elif keys_pressed[self.key_RIGHT] and self.rect.x + self.velocity + self.rect.width < WIDTH:
            self.rect.x += self.velocity
            self.direct = -90
        elif keys_pressed[self.key_UP] and self.rect.y - self.velocity > 0:
            self.rect.y -= self.velocity
            self.direct = 0
        elif keys_pressed[self.key_DOWN] and self.rect.y + self.velocity + self.rect.height < HEIGHT:
            self.rect.y += self.velocity
            self.direct = 180
        if keys_pressed[self.key_SHOOT] and self.delay == FPS:
            dx, dy, x_dir, y_dir = self.__direction_of_the_shoot()
            Bullet(self, x_dir, y_dir, dx, dy, self.direct)
            self.delay = 0 # скорость пули
        if self.delay != FPS:
            self.delay += 1
    def draw(self):
        #менять размер и направление
        if (self.colour == "yellow"):
            TANK_IMAGE = pygame.transform.rotate(pygame.transform.scale(TANKS_IMAGE[0], (TANK_SIZE, TANK_SIZE)), self.direct)
        else:
            TANK_IMAGE = pygame.transform.rotate(pygame.transform.scale(TANKS_IMAGE[1], (TANK_SIZE, TANK_SIZE)), self.direct)
        window.blit(TANK_IMAGE, (self.rect.x, self.rect.y))
class Bullet(ABC):
    """
    Создает пулю, двигает и отрисовывает на экране
    """
    def __init__(self, parent, x, y, v_x, v_y, direct):
        bullets.append(self)
        self.parent = parent
        self.x, self.y = x, y
        self.direct = direct
        self.v_x, self.v_y = v_x, v_y
    def __hit_border(self):
        if self.x > WIDTH or self.x < 0 or self.y > HEIGHT or self.y < 0:
            bullets.remove(self)
    def __hitting_rect_tank(self):
        for tank in tanks:
            if tank != self.parent and tank.rect.collidepoint(self.x, self.y):
                tanks.remove(tank)
                Boom(self.x, self.y)
                bullets.remove(self)
    def movement(self):
        self.x += self.v_x * BULLET_VELOCITY
        self.y += self.v_y * BULLET_VELOCITY
        self.__hit_border()
        self.__hitting_rect_tank()
    def draw(self):
        BULLET = pygame.transform.rotate(pygame.transform.scale(BULLET_IMAGE, (10, 12)), self.direct)
        window.blit(BULLET, (self.x, self.y))
class Boom(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.delay = 0
        self.size_of_boom = 16
        booms.append(self)
    def draw(self):
        if self.delay != FPS * 0.5:
            BOOM = pygame.transform.scale(BOOM_IMAGE, (self.size_of_boom, self.size_of_boom))
            window.blit(BOOM, (self.x - 24, self.y - 24))
            self.size_of_boom += 4
            self.delay += 1
        else:
            booms.remove(self)

init_tanks()
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS) # частота кадров в секунду
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys_pressed = pygame.key.get_pressed()
    for tank in tanks: tank.movement(keys_pressed)
    for bullet in bullets: bullet.movement()
    window.fill(BLACK)
    for tank in tanks: tank.draw()
    for bullet in bullets: bullet.draw()
    for boom in booms: boom.draw()
    pygame.display.update()
pygame.quit()
