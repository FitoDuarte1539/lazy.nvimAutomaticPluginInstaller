import curses
from curses import wrapper
import time


class Gui():
    def __init__(self, stdscr):
        curses.start_color()
        curses.use_default_colors()
        self.stdscr = stdscr
        curses.init_pair(1, curses.COLOR_BLUE, -1)
        curses.init_pair(2, curses.COLOR_YELLOW, -1)
        curses.init_pair(3, curses.COLOR_GREEN, -1)
        curses.init_pair(4, curses.COLOR_BLUE, -1)
        self.h, self.w = stdscr.getmaxyx()
        self.logo = """     __                _               ___             __ _                       _             
  /\ \ \___  _____   _(_)_ __ ___     / __\___  _ __  / _(_) __ _ _   _ _ __ __ _| |_ ___  _ __ 
 /  \/ / _ \/ _ \ \ / / | '_ ` _ \   / /  / _ \| '_ \| |_| |/ _` | | | | '__/ _` | __/ _ \| '__|
/ /\  /  __/ (_) \ V /| | | | | | | / /__| (_) | | | |  _| | (_| | |_| | | | (_| | || (_) | |   
\_\ \/ \___|\___/ \_/ |_|_| |_| |_| \____/\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__\___/|_|   """

    def main_menu(self, options=["No_Options"]):

        self.stdscr.clear()

        ypad = self.h // 20
        xpad = self.w // 20
        winx, winy = int(self.w - 2 * xpad), int(self.h - 2 * ypad)
        win = curses.newwin(winy, winx, ypad, xpad)

        win.keypad(True)

        win.attron(curses.color_pair(1))
        win.border()
        win.attroff(curses.color_pair(1))

        logo_lines = self.logo.splitlines()

        line_padding = " " * ((winx - 2 - max(len(item)
                              for item in logo_lines)) // 2)

        win.attron(curses.color_pair(2))
        for i, line in enumerate(logo_lines):
            win.addstr(i + 2, 1, line_padding + line + line_padding)
        win.attroff(curses.color_pair(2))

        self.display_options(win, options)

        win.refresh()

    def display_options(self, win, options=["Test1", "Test2", "Test3"]):

        current_option = 0

        start_line = len(self.logo.splitlines()) + 8

        total_space = self.h - start_line - 3

        spacing = total_space // (2 * len(options))

        while True:
            for i, option in enumerate(options):
                if i == current_option:
                    win.attron(curses.color_pair(3))
                else:
                    win.attron(curses.color_pair(4))

                win.addstr(start_line + i * spacing, 1,
                           self.center_align(option, win))

                win.attroff(curses.color_pair(3))
                win.attroff(curses.color_pair(4))

            win.refresh()

            key = win.getch()

            if key in [curses.KEY_UP, ord('w'), ord('W')] and current_option > 0:
                current_option -= 1
            elif key in [curses.KEY_DOWN, ord('s'), ord('S')] and (current_option < len(options) - 1):
                current_option += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                if options[current_option] == 'Quit':
                    break
                else:
                    pass
                # FIXME Add Implementation for moving To Different Menu's Here!
        win.clear()
        win.attron(curses.color_pair(1))
        win.border()
        win.attroff(curses.color_pair(1))
        self.stdscr.refresh()

    def center_align(self, string, win):
        _, winx = win.getmaxyx()
        return string.center(winx-2)


def main(stdscr):

    gui = Gui(stdscr)

    options = ["Install Plugins", "Configure Plugins",
               "Settings", "Help", "Quit"]

    gui.main_menu(options)


wrapper(main)
