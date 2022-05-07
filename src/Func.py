import sys
from random import randint

import pygame
from src.Tank import Tank

from src.Baza import Baza
from src.BlockFactory import BlockFactory
from src.Button import Button
from src.Enemy import Enemy
from src.Globals import Globals
from src.Images import Images
from src.Panel import Panel
from src.RebirthStar import RebirthStar
from src.UI import UI

pygame.init()
WIDTH, HEIGHT = 1280, 720
pygame.display.set_caption("Танчики")
window = pygame.display.set_mode((WIDTH, HEIGHT))


# создать танков игроков на карте, назначить на какие кнопки они будут двигаться и их скорость
def init_tanks(players, mode):
    if players == 1:
        Tank(378, Globals.HEIGHT - 96, Globals.VELOCITY, 0, 'yellow',
             (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_LCTRL), "coop")
    else:
        if mode == "coop":
            Tank(378, Globals.HEIGHT - 96, Globals.VELOCITY, 0, 'yellow',
                 (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_LCTRL), "coop")
            Tank(570, Globals.HEIGHT - 96, Globals.VELOCITY, 0, 'white',
                 (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_RCTRL), "coop")
        else:
            Tank(100, Globals.HEIGHT - 96, Globals.VELOCITY, 0, 'yellow',
                 (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_LCTRL), "vs_mode")
            Tank(1000, 100, Globals.VELOCITY, 0, 'white',
                 (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_RCTRL), "vs_mode")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def score(points):
    if points == 100:
        Globals.score_tanks[0][0] += points
        Globals.score_tanks[0][1] += 1
    elif points == 200:
        Globals.score_tanks[1][0] += points
        Globals.score_tanks[1][1] += 1
    else:
        Globals.score_tanks[2][0] += points
        Globals.score_tanks[2][1] += 1


# сбросить карту
def del_all():
    Globals.total = 0
    Globals.score_tanks = [[0, 0], [0, 0], [0, 0]]
    Globals.panels = []
    Globals.tanks = []
    Globals.enemies = []
    Globals.bullets = []
    Globals.waters = []
    Globals.booms = []
    Globals.brick_walls = []
    Globals.iron_blocks = []
    Globals.Russiantanks = []
    Globals.rebirth_stars = []
    Globals.soviettanks = []
    Globals.imperiantanks = []


def stage_coop():
    for i in range(0, Globals.WIDTH, 32):
        Panel(i, 0)
        Panel(i, Globals.HEIGHT - 32)
    for i in range(0, Globals.HEIGHT, 32):
        Panel(0, i)
        Panel(Globals.WIDTH - 32, i)
        Panel(Globals.WIDTH - 32 * 2, i)
        Panel(Globals.WIDTH - 32 * 3, i)
    factory = BlockFactory()
    for i in range(4):
        factory.get_block('brick', 110, 110 + 64 * i, Globals.TANK_SIZE, Globals.TANK_SIZE)
    for i in range(8):
        for j in range(2):
            factory.get_block('brick', 260 + 32 * j, 110 + 32 * i, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
    for i in range(6):
        for j in range(2):
            factory.get_block('brick', 410 + 32 * j, 110 + 32 * i, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
    for i in range(3):
        factory.get_block('brick', 538, 110 + 64 * i, Globals.TANK_SIZE, Globals.TANK_SIZE)
    for i in range(4):
        factory.get_block('brick', 688, 110 + 64 * i, Globals.TANK_SIZE, Globals.TANK_SIZE)
    for i in range(4):
        factory.get_block('brick', 838, 110 + 64 * i, Globals.TANK_SIZE, Globals.TANK_SIZE)
    for i in range(9):
        factory.get_block('water', 988, 32 + 64 * i)
    for i in range(9):
        factory.get_block('water', 1030, 32 + 64 * i)
    for i in range(9):
        factory.get_block('water', 1056, 32 + 64 * i)
    factory.get_block('brick', 32, 440, Globals.TANK_SIZE, Globals.TANK_SIZE / 2)
    factory.get_block('iron', 32, 472)
    factory.get_block('iron', 474, 192)
    factory.get_block('iron', 474, 224)
    for i in range(2):
        for j in range(4):
            factory.get_block('brick', 192 + 32 * j, 440 + 32 * i, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
    factory.get_block('brick', 924, 440, Globals.TANK_SIZE, Globals.TANK_SIZE / 2)
    factory.get_block('iron', 924, 472)
    for i in range(2):
        for j in range(4):
            factory.get_block('brick', 796 - 32 * j, 440 + 32 * i, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
    factory.get_block('brick', 538, 376, Globals.TANK_SIZE, Globals.TANK_SIZE)
    factory.get_block('brick', 410, 376, Globals.TANK_SIZE, Globals.TANK_SIZE)
    for i in range(3):
        factory.get_block('brick', 96 + 64 * i, 560 + 64, Globals.TANK_SIZE, Globals.TANK_SIZE)
    for i in range(3):
        factory.get_block('brick', 796 - 64 * i, 560 + 64, Globals.TANK_SIZE, Globals.TANK_SIZE)
    for i in range(3):
        factory.get_block('brick', 442, Globals.HEIGHT - 64 - 32 * i, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
        factory.get_block('brick', 538, Globals.HEIGHT - 64 - 32 * i, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
    factory.get_block('brick', 474, Globals.HEIGHT - 128, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
    factory.get_block('brick', 506, Globals.HEIGHT - 128, Globals.TANK_SIZE / 2, Globals.TANK_SIZE / 2)
    RebirthStar(32, 32)
    RebirthStar(474, 128)


def stage_vs():
    factory = BlockFactory()
    for i in range(0, Globals.WIDTH, 32):
        Panel(i, 0)
        Panel(i, Globals.HEIGHT - 32)
    for i in range(0, Globals.HEIGHT, 32):
        Panel(0, i)
        Panel(Globals.WIDTH - 32, i)
        Panel(Globals.WIDTH - 32 * 2, i)
        Panel(Globals.WIDTH - 32 * 3, i)
    for _ in range(69):
        while True:
            x = randint(0, (Globals.WIDTH - 32 * 3) // Globals.TANK_SIZE - 1) * Globals.TANK_SIZE
            y = randint(0, (Globals.HEIGHT - 32 * 2) // Globals.TANK_SIZE - 1) * Globals.TANK_SIZE
            rect = pygame.Rect(x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)
            check = False
            for tank in Globals.tanks:
                if rect.colliderect(tank.rect):
                    check = True
            for panel in Globals.panels:
                if rect.colliderect(panel.rect):
                    check = True
            for brick in Globals.brick_walls:
                if rect.colliderect(brick.rect):
                    check = True
            if not check:
                break
        factory.get_block('brick', x, y, Globals.TANK_SIZE, Globals.TANK_SIZE)


# генерация звездочек спавна
def reb_star_spawn(n):
    if len(Globals.Russiantanks) + len(Globals.soviettanks) + len(Globals.imperiantanks) < 4 \
            and Globals.total < 16:
        if n == 0:
            RebirthStar(32, 32)
        elif n == 1:
            RebirthStar(474, 128)
        elif n == 2:
            RebirthStar(Globals.WIDTH - 160, 32)
        else:
            RebirthStar(924, 32)


def play(players, mode):
    baza = Baza(474, Globals.HEIGHT - 96)
    del_all()
    ui = UI()
    init_tanks(players, mode)
    if mode == "coop":
        stage_coop()
    else:
        stage_vs()
    clock = pygame.time.Clock()
    run = True
    delay = 0
    if mode == "coop":
        Enemy(1)
    while run:
        clock.tick(Globals.FPS)  # частота кадров в секунду
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:
            pause()
        if mode == "vs_mode":
            for tank in Globals.tanks:
                tank.movement(keys_pressed)
            for bullet in Globals.bullets:
                bullet.movement()
            for brick_wall in Globals.brick_walls:
                brick_wall.update()
            for panel in Globals.panels:
                panel.update()
            window.fill((0, 0, 0))
            for panel in Globals.panels:
                panel.draw()
            for brick_wall in Globals.brick_walls:
                brick_wall.draw()
            for tank in Globals.tanks:
                tank.draw()
            for bullet in Globals.bullets:
                bullet.draw()
            for boom in Globals.booms:
                boom.draw()
            ui.draw()
            pygame.display.update()
        else:
            n = randint(0, 4)
            if delay == Globals.FPS + 60:
                delay = 0
                reb_star_spawn(n)
            else:
                delay += 1
            baza.update()
            for enemy in Globals.enemies:
                enemy.update()
            for tank in Globals.tanks:
                tank.movement(keys_pressed)
            for bullet in Globals.bullets:
                bullet.movement()
            for brick_wall in Globals.brick_walls:
                brick_wall.update()
            for iron_wall in Globals.iron_blocks:
                iron_wall.update()
            for panel in Globals.panels:
                panel.update()
            for russian_tank in Globals.Russiantanks:
                russian_tank.movement()
            for soviettank in Globals.soviettanks:
                soviettank.movement()
            for imperiantank in Globals.imperiantanks:
                imperiantank.movement()
            window.fill((0, 0, 0))
            baza.draw()
            for water in Globals.waters:
                water.draw()
            for imperiantank in Globals.imperiantanks:
                imperiantank.draw()
            for soviettank in Globals.soviettanks:
                soviettank.draw()
            for rebirth_star in Globals.rebirth_stars:
                rebirth_star.draw()
            for russian_tank in Globals.Russiantanks:
                russian_tank.draw()
            for panel in Globals.panels:
                panel.draw()
            for iron_wall in Globals.iron_blocks:
                iron_wall.draw()
            for brick_wall in Globals.brick_walls:
                brick_wall.draw()
            for tank in Globals.tanks:
                tank.draw()
            for bullet in Globals.bullets:
                bullet.draw()
            for boom in Globals.booms:
                boom.draw()
            for enemy in Globals.enemies:
                enemy.draw()
            ui.draw()
            pygame.display.update()
    pygame.quit()


def mode():
    pause = True
    while pause:
        window.blit(Images.BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("PAUSE", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        cooperative_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250),
                                    text_input="COOPERATIVE", font=get_font(50), base_color="#d7fcd4",
                                    hovering_color="White")
        back_to_menu = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                              text_input="BACK TO MENU", font=get_font(47), base_color="#d7fcd4",
                              hovering_color="White")
        vs_mode = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 550),
                         text_input="Tank vs Tank", font=get_font(47), base_color="#d7fcd4", hovering_color="White")

        window.blit(menu_text, menu_rect)

        for button in [cooperative_button, back_to_menu, vs_mode]:
            button.changeColor(menu_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cooperative_button.checkForInput(menu_mouse_pos):
                    play(2, 'coop')
                if back_to_menu.checkForInput(menu_mouse_pos):
                    main_menu()
                if vs_mode.checkForInput(menu_mouse_pos):
                    play(2, "vs_mode")
        pygame.display.update()


def main_menu():
    while True:
        window.blit(Images.BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        player_1_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250),
                                 text_input="1 PLAYER", font=get_font(70), base_color="#d7fcd4", hovering_color="White")
        player_2_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                 text_input="2 PLAYER", font=get_font(70), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        window.blit(menu_text, menu_rect)

        for button in [player_1_button, player_2_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_1_button.checkForInput(menu_mouse_pos):
                    play(1, "coop")
                if player_2_button.checkForInput(menu_mouse_pos):
                    mode()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def score_menu(stat, mode):
    while True:
        window.blit(Images.BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("SCORE MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))
        if mode == "coop":
            if stat:
                statistic = Button(image=None, pos=(640, 200),
                                   text_input="YOU WIN!!!", font=get_font(58), base_color="#d7fcd4",
                                   hovering_color="White")
            else:
                statistic = Button(image=None, pos=(640, 200),
                                   text_input="YOU LOSE!!", font=get_font(58), base_color="#d7fcd4",
                                   hovering_color="White")
        else:
            if stat:
                statistic = Button(image=None, pos=(640, 200),
                                   text_input="YELLOW WINS!", font=get_font(58), base_color="#d7fcd4",
                                   hovering_color="White")
            else:
                statistic = Button(image=None, pos=(640, 200),
                                   text_input="WHITE WINS!", font=get_font(58), base_color="#d7fcd4",
                                   hovering_color="White")
        back_to_menu = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(350, 500),
                              text_input="BACK TO MENU", font=get_font(40), base_color="#d7fcd4",
                              hovering_color="White")

        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1000, 500),
                             text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        window.blit(menu_text, menu_rect)

        for button in [back_to_menu, quit_button, statistic]:
            button.changeColor(menu_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_menu.checkForInput(menu_mouse_pos):
                    main_menu()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def pause():
    pause = True
    while pause:
        window.blit(Images.BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("PAUSE", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        continue_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250),
                                 text_input="CONTINUE", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        back_to_menu = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                              text_input="BACK TO MENU", font=get_font(47), base_color="#d7fcd4",
                              hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        window.blit(menu_text, menu_rect)

        for button in [continue_button, back_to_menu, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.checkForInput(menu_mouse_pos):
                    pause = False
                if back_to_menu.checkForInput(menu_mouse_pos):
                    main_menu()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
