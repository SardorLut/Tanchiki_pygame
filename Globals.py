import pygame


class Globals:
    # переменные
    FPS = 30
    total = 0
    VELOCITY = 6
    BULLET_VELOCITY = 18
    TANK_SIZE = 64
    # списки
    panels = []
    tanks = []
    bullets = []
    booms = []
    waters = []
    enemies = []
    brick_walls = []
    iron_blocks = []
    Russiantanks = []
    rebirth_stars = []
    soviettanks = []
    WIDTH, HEIGHT = 1280, 720
    imperiantanks = []
    score_tanks = [[0, 0], [0, 0], [0, 0]]
    window = pygame.display.set_mode((WIDTH, HEIGHT))
