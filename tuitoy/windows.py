"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

import curses

class Window:
    # Name: __init__
    # Parameters: (int) x, (int) y, (int) width, (int) height, (bool) border
    # Returns: None
    # Description: Constructor for Window object
    def __init__(self, x=0, y=0, width=0, height=0, border=False):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__border = border
        self.__entities = []
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    # Name: get_x
    # Parameters: None
    # Returns: (int) x
    # Description: Returns the x coordinate of the window
    def get_x(self):
        return self.__x

    # Name: set_x
    # Parameters: (int) x
    # Returns: None
    # Description: Sets the x coordinate of the window
    def set_x(self, x):
        self.__x = x
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    # Name: get_y
    # Parameters: None
    # Returns: (int) y
    # Description: Returns the y coordinate of the window
    def get_y(self):
        return self.__y

    # Name: set_y
    # Parameters: (int) y
    # Returns: None
    # Description: Sets the y coordinate of the window
    def set_y(self, y):
        self.__y = y
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    # Name: get_width
    # Parameters: None
    # Returns: (int) width
    # Description: Returns the width of the window
    def get_width(self):
        return self.__width

    # Name: set_width
    # Parameters: (int) width
    # Returns: None
    # Description: Sets the width of the window
    def set_width(self, width): 
        self.__width = width
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    # Name: get_height
    # Parameters: None
    # Returns: (int) height
    # Description: Returns the height of the window
    def get_height(self):
        return self.__height

    # Name: set_height
    # Parameters: (int) height
    # Returns: None
    # Description: Sets the height of the window
    def set_height(self, height):
        self.__height = height
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    # Name: get_border
    # Parameters: None
    # Returns: (bool) border
    # Description: Returns whether the window has a border
    def get_border(self):
        return self.__border

    # Name: set_border
    # Parameters: (bool) border
    # Returns: None
    # Description: Sets whether the window has a border
    def set_border(self, border):
        self.__border = border

    # Name: get_border_color
    # Parameters: None
    # Returns: (int) border_color
    # Description: Returns the color of the border
    def add_entity(self, entity):
        self.__entities.append(entity)

    # Name: set_border_color
    # Parameters: (int) border_color
    # Returns: None
    # Description: Sets the color of the border
    def remove_entity(self, entity):
        self.__entities.remove(entity)

    # Name: render
    # Parameters: (cursses.window) stdscr
    # Returns: None
    # Description: Renders the window
    def render(self, stdscr):
        if self.__border:
            self.__window.box()
        if self.__entities:
            for entity in self.__entities:
                entity.render(stdscr)

    def refresh(self):
        self.__window.refresh()

class Text_Window(Window):
    # Name: __init__
    # Parameters: (int) x, (int) y, (int) width, (int) height, (bool) border
    # Returns: None
    # Description: Constructor for Text_Window object
    def __init__(self, x=0, y=0, width=0, height=0, border=False, text=[], text_align="left"):
        super().__init__(x, y, width, height, border)
        self.__text = text
        self.__text_align = text_align

    # Name: render
    # Parameters: (cursses.window) stdscr
    # Returns: None
    # Description: Renders the Text_Window
    def render(self, stdscr):
        if self.__text_align == "left":
            for i in range(len(self.__text)):
                stdscr.addstr(self.get_y() + i, self.get_x(), self.__text[i])
        elif self.__text_align == "center":
            for i in range(len(self.__text)):
                stdscr.addstr(self.get_y() + i, self.get_x() + (self.get_width() - len(self.__text[i])) // 2, self.__text[i])
        elif self.__text_align == "right":
            for i in range(len(self.__text)):
                stdscr.addstr(self.get_y() + i, self.get_x() + self.get_width() - len(self.__text[i]), self.__text[i])
        super().render(stdscr)

"""
Copyright (C) 2023 Austin Choi
All rights reserved.

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
