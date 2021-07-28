import pygame
import random

# Game Initialization
pygame.init()

# Main Window
XDimension = 800
YDimension = 600
screen = pygame.display.set_mode((XDimension, YDimension))

# Player
main_player = pygame.image.load('ship.png')
main_playerX = 370
main_playerY = 500
main_playerChangeX = 0
main_playerChangeY = 0

# Enemy
main_enemy = pygame.image.load('enemy.png')
main_enemyX = random.randint(10, 730)
main_enemyY = random.randint(70, 150)
main_enemyChangeX = 0.4
main_enemyChangeY = 0.4
# Bullet
main_bullet = pygame.image.load('bullet.png')
main_bulletX = 0
main_bulletY = 500
# main_bulletChangeX = 0.4
main_bulletChangeY = 2
bullet_state = False
# Title
pygame.display.set_caption('Mah First Gayme')


# Player draw to screen
def player(x, y):
    screen.blit(main_player, (x, y))


# Enemy draw to screen
def enemy(x, y):
    screen.blit(main_enemy, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = True
    screen.blit(main_bullet, (x + 16, y + 10))


# Event Loop
run = True
while run:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                main_playerChangeX = -0.6

            if event.key == pygame.K_d:
                main_playerChangeX = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state is False:
                    main_bulletX = main_playerX
                    fire_bullet(main_bulletX, main_bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                main_playerChangeX = 0
                main_playerChangeY = 0


    # Movement and Boundaries
    # Player Movement
    main_playerX += main_playerChangeX
    main_playerY += main_playerChangeY
    if main_playerX <= 0:
        main_playerX = 0
    if main_playerX >= 736:
        main_playerX = 736

    # Enemy Movement
    main_enemyX += main_enemyChangeX

    if main_enemyX <= 0:
        main_enemyChangeX = 0.3
        main_enemyY += 30
    if main_enemyX >= 736:
        main_enemyChangeX = -0.3
        main_enemyY += 30
    if main_enemyY <= 0:
        main_enemyY = 0
    if main_enemyY >= 546:
        main_enemyY = 546

    # Bullet Movement

    if bullet_state is True:
        fire_bullet(main_bulletX, main_bulletY)
        main_bulletY -= main_bulletChangeY
    if main_bulletY <= 5:
        main_bulletY = 500
        bullet_state = False

    player(main_playerX, main_playerY)
    enemy(main_enemyX, main_enemyY)
    pygame.display.update()
