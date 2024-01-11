"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

import curses

class Window:
    def __init__(self, x=0, y=0, width=0, height=0, border=False):
        """
                Constructor for the Window object

                Parameters:
                        x (int): The x coordinate of the window
                        y (int): The y coordinate of the window
                        width (int): The width of the window
                        height (int): The height of the window
                        border (bool): Whether or not the window has a border
                Returns:
                        None
                        
        """
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__border = border
        self.__entities = []
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    def get_x(self):
        """
                Returns the x coordinate of the window

                Parameters:
                        None
                Returns:
                        (int): The x coordinate of the window
        """
        return self.__x

    def set_x(self, x):
        """
                Sets the x coordinate of the window

                Parameters:
                        x (int): The new x coordinate of the window
                Returns:
                        None
        """
        self.__x = x
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    def get_y(self):
        """
                Returns the y coordinate of the window
                
                Parameters:
                        None
                Returns:
                        (int): The y coordinate of the window
        """
        return self.__y

    def set_y(self, y):
        """
                Sets the y coordinate of the window

                Parameters:
                        y (int): The new y coordinate of the window
                Returns:
                        None
        """
        self.__y = y
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    def get_width(self):
        """
                Returns the width of the window

                Parameters:
                        None
                Returns:
                        (int): The width of the window
        """
        return self.__width

    def set_width(self, width):
        """
                Sets the width of the window
                
                Parameters:
                        width (int): The new width of the window
                Returns:
                        None
        """
        self.__width = width
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    def get_height(self):
        """
                Returns the height of the window

                Parameters:
                        None
                Returns:
                        (int): The height of the window
        """
        return self.__height

    def set_height(self, height):
        """
                Sets the height of the window

                Parameters:
                        height (int): The new height of the window
                Returns:
                        None
        """
        self.__height = height
        self.__window = curses.newwin(self.__height, self.__width, self.__y, self.__x)

    def get_border(self):
        """
                Returns whether the window has a border

                Parameters:
                        None
                Returns:
                        (bool): Whether the window has a border
        """
        return self.__border

    def set_border(self, border):
        """
                Sets whether the window has a border

                Parameters:
                        border (bool): Whether the window has a border
                Returns:
                        None
        """
        self.__border = border

    def add_entity(self, entity):
        """
                Adds an entity to the window
                
                Parameters:
                        entity (Entity): The entity to be added
                Returns:
                        None
        """
        self.__entities.append(entity)

    def remove_entity(self, entity):
        """
                Removes an entity from the window

                Parameters:
                        entity (Entity): The entity to be removed
                Returns:
                        None
        """
        self.__entities.remove(entity)

    def render(self, stdscr):
        """
                Renders the window

                Parameters:
                        stdscr (curses.window): The window to render to
                Returns:
                        None
        """
        if self.__border:
            self.__window.box()
        if self.__entities:
            for entity in self.__entities:
                entity.render(stdscr)

    def refresh(self):
        """
                Refreshes the window

                Parameters:
                        None
                Returns:
                        None
        """
        self.__window.refresh()

class Text_Window(Window):
    def __init__(self, x=0, y=0, width=0, height=0, border=False, text=[], text_align="left"):
        """
                Constructor for the Text_Window object

                Parameters:
                        x (int): The x coordinate of the window
                        y (int): The y coordinate of the window
                        width (int): The width of the window
                        height (int): The height of the window
                        border (bool): Whether or not the window has a border
                        text (list): The text to be displayed in the window
                        text_align (string): The alignment of the text
                Returns:
                        None
        """
        super().__init__(x, y, width, height, border)
        self.__text = text
        self.__text_align = text_align

    def render(self, stdscr):
        """
                Renders the Text_Window

                Parameters:
                        stdscr (curses.window): The window to render to
                Returns:
                        None
        """
        super().render(stdscr)
        
        if self.__text_align == "left":
            for i in range(len(self.__text)):
                stdscr.addstr(super().get_y() + 1 + i, super().get_x() + 1, self.__text[i])
        elif self.__text_align == "center":
            for i in range(len(self.__text)):
                stdscr.addstr(super().get_y() + 1+ i, super().get_x() + (super().get_width() - len(self.__text[i])) // 2, self.__text[i])
        elif self.__text_align == "right":
            for i in range(len(self.__text)):
                stdscr.addstr(super().get_y() + 1 + i, (super().get_x() + super().get_width() - len(self.__text[i])) - 1, self.__text[i])

"""
Copyright (C) 2023 Austin Choi
All rights reserved.

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
