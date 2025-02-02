import curses

def main(stdscr):
    # Setup color pair (optional)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    # Clear screen
    stdscr.clear()

    # Define window size and position
    height, width = 10, 30
    win = curses.newwin(height, width, 5, 5)  # Create a new window with given size

    # Custom small border characters
    border_vertical = '|'
    border_horizontal = '-'
    
    # Draw the custom border (top, bottom, left, right)
    for y in range(height):
        for x in range(width):
            if y == 0 or y == height - 1:  # Top and bottom borders
                win.addch(y, x, border_horizontal)
            elif x == 0 or x == width - 1:  # Left and right borders
                win.addch(y, x, border_vertical)
    
    # Add some text inside the window with color
    win.addstr(2, 2, "Hello, world!", curses.color_pair(1))

    # Refresh the window to display
    win.refresh()
    
    # Wait for user input before quitting
    stdscr.getch()

# Start the curses application
curses.wrapper(main)

