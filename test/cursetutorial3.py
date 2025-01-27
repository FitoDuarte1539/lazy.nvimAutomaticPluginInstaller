import curses
from curses import wrapper
import time


def gui(stdscr):
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    x, y = 0, 0
    while True:
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_DOWN":
            y += 1
        elif key == "KEY_UP":
            y -= 1

        stdscr.clear()
        stdscr.addstr(y, x, "0")
        stdscr.refresh()


wrapper(gui)
