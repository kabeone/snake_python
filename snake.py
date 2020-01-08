import curses
import random
import math

s = curses.initscr()

curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = math.floor(sw/4)
snk_y = math.floor(sh/4)
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [math.floor(sh / 2), math.floor(sw / 2)]
w.addch(food[0], food[1], curses.ACS_PI)
key = curses.KEY_RIGHT
score = 0
i = 0

while i < sh - 1:
    w.addch(i, 0, '#')
    w.addch(i, sw - 1, '#')
    i += 1
i = 0
while i < sw - 1:
    w.addch(0, i, '#')
    w.addch((sh - 1), i, '#')
    i += 1

i = 0

while True:
    next_key = w.getch()

    if next_key == -1:
        key = key
    elif key == curses.KEY_UP and next_key == curses.KEY_DOWN:
        key = key
    elif key == curses.KEY_DOWN and next_key == curses.KEY_UP:
        key = key
    elif key == curses.KEY_LEFT and next_key == curses.KEY_RIGHT:
        key = key
    elif key == curses.KEY_RIGHT and next_key == curses.KEY_LEFT:
        key = key
    else:
        key = next_key

    if snake[0][0] in [0, sh - 1] or snake[0][1] in [0, sw - 1] or snake[0] in snake[1:]:
        curses.endwin()
        print("score :", score)
        quit()

    new_head = [snake[0][0], snake[0][1]]
    b = new_head

    if key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1
    else:
        continue

    snake.insert(0, new_head)
    if food in snake:
        food = None
        while food is None:
            score += 1
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1),
            ]
            if nf not in snake:
                food = nf
            else:
                food = None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(math.floor(tail[0]), math.floor(tail[1]), ' ')

    w.addch(math.floor(snake[0][0]), math.floor(snake[0][1]), curses.ACS_CKBOARD)
