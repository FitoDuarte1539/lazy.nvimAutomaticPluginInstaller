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

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_AND_BLACK)
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, i, 5, i, 10, 25 + i)
        time.sleep(0.2)
    stdscr.getch()


wrapper(gui)
