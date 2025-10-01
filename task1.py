import pygame as pg

# здесь определяются константы, функции и классы
FPS = 60
WIDTH, HEIGHT = 1000, 600
BLUE = (0, 0, 255)
MINT = (166, 255, 169)
BROWN = (71, 36, 36)
YELLOW = 243, 255, 0
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 11, 107, 0

# здесь происходит инициализация, создание объектов
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))  # также здесь можно указать битовые флаги
screen.fill(MINT)
pg.display.set_caption("Игра")
clock = pg.time.Clock()


# house_x =
# house_y =
# door_width
# door_he

pg.draw.rect(screen, BROWN , (450, 250, 200, 200))
pg.draw.polygon(screen, RED, [[449,250], [550, 50], [650, 250]])
pg.draw.circle(screen, YELLOW, (100, 100), 50)
pg.draw.rect(screen, BLACK, (480, 350, 50, 75))
pg.draw.rect(screen, BLUE , (580, 280, 50, 50))
pg.draw.rect(screen, GREEN  , (0, 450, 1000, 1000))
pg.display.update()


flag_play = True
while flag_play:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение объектов
    # ...

    # обновление экрана
    pg.display.update()







