import pygame as pg
from random import randrange

pg.init()

diddenblud_window = 1000
diddenblud_screen = pg.display.set_mode([diddenblud_window] * 2)
diddenblud_clock = pg.time.Clock()
sussyblud_tile_size = 50
sussyblud_range = (sussyblud_tile_size // 2, diddenblud_window - sussyblud_tile_size // 2, sussyblud_tile_size)
# erratic is synonymous with random
get_erratic_position = lambda: [randrange(*sussyblud_range), randrange(*sussyblud_range)]
# making the snake spawn in a random position, to add spice if you will
that_guy_from_snake_game = pg.rect.Rect([0, 0, sussyblud_tile_size - 2, sussyblud_tile_size - 2])
that_guy_from_snake_game.center = get_erratic_position()
# snake direction
that_guy_from_snake_game_dir = (0, 0)
length = 1
segments = [that_guy_from_snake_game.copy()]
# much needed delay
time, time_step = 0, 110
# now for the infamous apple made green
green_apple = that_guy_from_snake_game.copy()
green_apple.center = get_erratic_position()
# something to make so that the snake can move in opposite directions
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
#font for the score counter
font = pg.font.SysFont('Comic Sans MS', 30)

while True:
    # checks if you quit the game or not
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                that_guy_from_snake_game_dir = (0, -sussyblud_tile_size)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and dirs[pg.K_s]:
                that_guy_from_snake_game_dir = (0, sussyblud_tile_size)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a]:
                that_guy_from_snake_game_dir = (-sussyblud_tile_size, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_d and dirs[pg.K_d]:
                that_guy_from_snake_game_dir = (sussyblud_tile_size, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
        # game logic timeee
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
    # i am never developing games, ever. only if it's for like projects and stuff, but i am not doing games for the life of me.
        # moving the snake, in which I, the chosen one, am going to attempt to make the claimed snake heads follow the main snake head, leaving "footsteps" behind
        that_guy_from_snake_game.move_ip(that_guy_from_snake_game_dir)
        segments.append(that_guy_from_snake_game.copy())
        segments = segments[-length:]
        # my fucking code failed (though, as you're reading this, it probably means i fixed the code, just a documentation of my thoughts)
        # time to make borders, because what's a country without one? also since we're in a "country" let's make laws so that people can't eat themselves.
        self_eating = pg.Rect.collidelist(that_guy_from_snake_game, segments[:-1]) != -1
        if (
    that_guy_from_snake_game.left < 0 or
    that_guy_from_snake_game.right > diddenblud_window or
    that_guy_from_snake_game.top < 0 or
    that_guy_from_snake_game.bottom > diddenblud_window or
    self_eating
):
            that_guy_from_snake_game.center = get_erratic_position()
            green_apple.center = get_erratic_position()
            length = 1
            that_guy_from_snake_game_dir = (0, 0)
            segments = [that_guy_from_snake_game.copy()]
        # this section was MUCH more complicated than i expected it to be.
        # and now, to check for the position of the food and the snake, if they're both in the same position, add length to snake.
        if that_guy_from_snake_game.center == green_apple.center:
            green_apple.center = get_erratic_position()
            length += 1
        # ohhh this executed first try i'm so damn happy
        # drawing time, i was never a good drawer but oh well
        diddenblud_screen.fill('black')
        # the green apple in question:
        pg.draw.rect(diddenblud_screen, 'green', green_apple)
        # fym rect argument is invalid?? i'll find a workaround, istg this language (this wasn't the problem, absolute cinema)
        # making that god damn snake, using red for snake and green for apple, for no particular reason other than making the game slightly confusing
        [pg.draw.rect(diddenblud_screen, 'red', segment) for segment in segments]
        # and now, the score counter
        score_text = font.render(f'Green apples counter: {length}', True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, diddenblud_window - score_rect.height - 10)
        diddenblud_screen.blit(score_text, score_rect)
        diddenblud_clock.tick(60)
        pg.display.flip()