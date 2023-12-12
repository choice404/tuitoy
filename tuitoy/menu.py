"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

import curses

class Menu:
    # Constructor for the menu object
    def __init__(self, window, menu_map = {"init": []}, left = 'a', right = 'd'):
        self.__window = window
        self.__width = self.__window.max_width - (8 * self.__window.per_width)
        self.__height = self.__window.max_height - 1
        self.__x = 4 * self.__window.per_width
        self.__y = self.__height - 5
        self.__selected = 0
        self.__menu_map = menu_map
        self.__current_menu = self.__menu_map["init"]
        self.__menu_length = len(self.__current_menu)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_GREEN)
        # curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.__left = ord(left)
        self.__right = ord(right)
        self.__menu_arrow = False

    # Name: get_direction_keys
    # Parameters: self
    # Return: int self.__left, int self.__right
    # Description: Returns the values to be used to navigate the menu
    def get_direction_keys(self):
        if self.__menu_arrow:
            return [self.__left, curses.KEY_LEFT], [self.__right, curses.KEY_RIGHT]
        return [self.__left], [self.__right]

    # Name: move_cursor
    # Parameters: self, int dir
    # Return: int self.__selected
    # Description: Will change what menu item is selected
    def move_cursor(self, dir):
        self.__selected += dir
        if self.__selected == self.__menu_length:
            self.__selected -= 1
        elif self.__selected < 0:
            self.__selected += 1
        return self.__selected

    # Name: menu_arrow_set
    # Parameters: self
    # Return: bool self.__menu_arrow
    # Description: Menu will be controlled with arrow keys
    def menu_arrow_set(self):
        self.__menu_arrow = True
        return self.__menu_arrow

    # Name: menu_arrow_unset
    # Parameters: self
    # Return: bool self.__menu_arrow
    # Description: Menu will be controlled with the self.__left and self.__right characters
    def menu_arrow_unset(self):
        self.__menu_arrow = False
        return self.__menu_arrow

    # Name: set_menu
    # Parameters: self, string menu_name
    # Return: N/A
    # Description: Changes which menu to display
    def set_menu(self, menu_name):
        self.__current_menu = self.__menu_map[menu_name]
        self.__menu_length = len(self.__current_menu)

    # Name: append_menu_map
    # Parameters: self, string menu_name, string[] menu
    # Return: N/A
    # Description: Adds new menu to the menu map as a key value pair
    def append_menu_map(self, menu_name, menu):
        self.__menu_map[menu_name] = menu

    # Name: draw
    # Parameters: self, stdscr
    # Return: N/A
    # Description: Draws the menu on the screen
    def draw(self, stdscr):
        menu_display_length = (self.__menu_length * 3) + 1
        __row = '-' * self.__width
        for i in self.__current_menu:
            menu_display_length += len(i)

        menu_x = (self.__window.get_max_width() - menu_display_length) // 2

        stdscr.addstr(self.__y, self.__x, __row)
        stdscr.addstr(self.__y + 4, self.__x, __row)
        stdscr.addch(self.__y + 1, self.__x, '|')
        stdscr.addch(self.__y + 1, self.__width + self.__x - 1, '|')
        stdscr.addch(self.__y + 2, self.__x, '|')
        stdscr.addch(self.__y + 2, self.__width + self.__x - 1, '|')
        stdscr.addch(self.__y + 3, self.__x, '|')
        stdscr.addch(self.__y + 3, self.__width + self.__x - 1, '|')

        runningX = menu_x + 1
        # stdscr.addstr(self.__y + 1, runningX, str(runningX))
        stdscr.addch(self.__y + 1, runningX, '|')
        stdscr.addch(self.__y + 2, runningX, '|')
        stdscr.addch(self.__y + 3, runningX, '|')
        runningX += 2
        for i, menu_item in enumerate(self.__current_menu):
            item = menu_item

            if self.__selected == i:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(self.__y + 2, runningX, item)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(self.__y + 2, runningX, item)
            runningX += len(item) + 1
            # stdscr.addstr(self.__y + 1, runningX, str(self.__window.get_max_width() - runningX))
            stdscr.addch(self.__y + 1, runningX, '|')
            stdscr.addch(self.__y + 2, runningX, '|')
            stdscr.addch(self.__y + 3, runningX, '|')
            # stdscr.addstr(self.__y + 3, runningX, str(menu_display_length))
            runningX += 2

    def refresh(self):
        self.__width = self.__window.max_width - (8 * self.__window.per_width)
        self.__height = self.__window.max_height - 1
        self.__x = 4 * self.__window.per_width
        self.__y = self.__height - 5

def main():
  # Enter code here
  print("menu.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
