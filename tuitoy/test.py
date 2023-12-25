import curses

def scroll_window(stdscr, content):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Get the size of the terminal window
    height, width = stdscr.getmaxyx()

    # Define the size of the scrollable area
    scrollable_height = height - 20 #min(height - 2, len(content))
    scrollable_width = width - 20

    # Create a window for displaying the scrollable area
    scroll_win = curses.newwin(scrollable_height, scrollable_width, 1, 1)

    # Initialize variables for scrolling
    start_row = 0

    # Main loop
    while True:
        # Clear the scrollable window
        scroll_win.clear()

        # Display a portion of the content based on the start_row
        for i in range(scrollable_height):
            if start_row + i < len(content):
                scroll_win.addstr(i, 0, content[start_row + i])

        # Draw a border around the scrollable window
        scroll_win.box()

        # Refresh the screen
        stdscr.refresh()
        scroll_win.refresh()

        # Get user input
        key = stdscr.getch()

        # Handle user input
        if key == curses.KEY_UP and start_row > 0:
            start_row -= 1
        elif key == curses.KEY_DOWN and start_row < len(content) - scrollable_height:
            start_row += 1
        elif key == ord('q'):
            break

curses.wrapper(scroll_window, ["Line {}".format(i) for i in range(100)])
