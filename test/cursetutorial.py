import curses
from curses import wrapper


def gui(stdscr):
    curses.start_color()
    curses.use_default_colors()
    stdscr.clear()
    stdscr.addstr(10, 20, "Hello World!", curses.A_BOLD)
    stdscr.addstr(11, 30, "Hello World!")
    stdscr.refresh()
    stdscr.getch()


wrapper(gui)
