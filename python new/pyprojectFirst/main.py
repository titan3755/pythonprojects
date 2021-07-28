import pygame as pg

#Screen Variables
winX = 1280
winY = 720

pg.init()
screen = pg.display.set_mode((winX, winY))
pg.display.set_caption('First Game')

def draw_rect():
    pg.draw.rect(screen, (255,255,255), pg.Rect(20, 30, 50, 60), 1, 10)

def main():
    game_running = True
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
        draw_rect()
        pg.display.update()
    pg.quit()

main()

