import pygame as pg
from random import randrange

pg.init()

window = 1000
screen = pg.display.set_mode([window] * 2)
clock = pg.time.Clock()
tile_size = 50
range = (tile_size // 2, window - tile_size // 2, tile_size)
# position where the snake and apple will spawn
get_random_position = lambda: [randrange(*range), randrange(*range)]
# making the snake spawn in a random position
snake = pg.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
snake.center = get_random_position()
# snake direction
snake_dir = (0, 0)
length = 1
segments = [snake.copy()]
time, time_step = 0, 110
# the infamous apple made green
green_apple = snake.copy()
green_apple.center = get_random_position()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
# font for the score counter
font = pg.font.SysFont('Comic Sans MS', 30)

while True:
    # checks if you quit the game or not
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -tile_size)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0, tile_size)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-tile_size, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (tile_size, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
        # game logic
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
        # borders
        self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if (
    snake.left < 0 or
    snake.right > window or
    snake.top < 0 or
    snake.bottom > window or
    self_eating
):
            snake.center = get_random_position()
            green_apple.center = get_random_position()
            length = 1
            snake_dir = (0, 0)
            segments = [snake.copy()]
        # check for the position of the food and the snake, if they're both in the same position, add length to snake.
        if snake.center == green_apple.center:
            green_apple.center = get_random_position()
            length += 1
        # draw
        screen.fill('black')
        pg.draw.rect(screen, 'green', green_apple)
        [pg.draw.rect(screen, 'red', segment) for segment in segments]
        # and now, the score counter
        score_text = font.render(f'Green apples counter: {length}', True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, window - score_rect.height - 10)
        screen.blit(score_text, score_rect)
        clock.tick(60)
        pg.display.flip()
