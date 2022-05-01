import pygame
import os


class Images:
    TANKS_IMAGE = [pygame.image.load(os.path.join('assets', 'tank_1.png')),
                   pygame.image.load(os.path.join('assets', 'tank_2.png')),
                   pygame.image.load(os.path.join('assets', 'red_tank_1.png')),
                   pygame.image.load(os.path.join('assets', 'red_tank_2.png')),
                   pygame.image.load(os.path.join('assets', 'red_tank_3.png')),
                   pygame.image.load(os.path.join('assets', 'green_tank_1.png')),
                   pygame.image.load(os.path.join('assets', 'green_tank_2.png')),
                   pygame.image.load(os.path.join('assets', 'green_tank_3.png')), ]

    BULLET_IMAGE = pygame.image.load(os.path.join('assets', 'bullet.png'))
    BOOMS_IMAGE = [pygame.image.load(os.path.join('assets', 'boom_1.png')),
                   pygame.image.load(os.path.join('assets', 'boom_2.png')),
                   pygame.image.load(os.path.join('assets', 'boom_3.png')),
                   pygame.image.load(os.path.join('assets', 'boom_4.png')),
                   pygame.image.load(os.path.join('assets', 'boom_5.png'))]
    LIFE_IMAGE = pygame.image.load(os.path.join('assets', 'life.png'))
    WALL_IMAGE = [pygame.image.load(os.path.join('assets', 'block_brick_1.png')),
                  pygame.image.load(os.path.join('assets', 'block_brick_2.png')),
                  pygame.image.load(os.path.join('assets', 'block_brick.png'))]
    IRON_BLOCK_IMAGE = pygame.image.load(os.path.join('assets', 'iron_block_2.png'))
    WATER_IMAGE = [pygame.image.load(os.path.join('assets', 'water_1.png')),
                   pygame.image.load(os.path.join('assets', 'water_3.png'))]
    PANEL_IMAGE = pygame.image.load(os.path.join('assets', 'panel.png'))
    BAZA_IMAGE = pygame.image.load(os.path.join('assets', 'eagle.png'))
    PLAYER_1_IMAGE = pygame.image.load(os.path.join('assets', '1_player.png'))
    PLAYER_2_IMAGE = pygame.image.load(os.path.join('assets', '2_player.png'))
    PLAYER_LIFE_IMAGE = pygame.image.load(os.path.join('assets', 'player_life.png'))
    REBIRTH_1_IMAGE = pygame.image.load(os.path.join('assets', 'rebirth_1.png'))
    REBIRTH_2_IMAGE = pygame.image.load(os.path.join('assets', 'rebirth_2.png'))
    REBIRTH_3_IMAGE = pygame.image.load(os.path.join('assets', 'rebirth_3.png'))
    REBIRTH_4_IMAGE = pygame.image.load(os.path.join('assets', 'rebirth_4.png'))
    BG = pygame.image.load("assets/Background.png")
