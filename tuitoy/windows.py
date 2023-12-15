"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

import curses

class Window:
    def __init__(self, x=0, y=0, width=0, height=0, border=False, border_color=0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__border = border
        self.__border_color = border_color
        self.__entities = []

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width): 
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_border(self):
        return self.__border

    def set_border(self, border):
        self.__border = border

    def get_border_color(self):
        return self.__border_color

    def set_border_color(self, border_color):
        self.__border_color = border_color

    def add_entity(self, entity):
        self.__entities.append(entity)

    def remove_entity(self, entity):
        self.__entities.remove(entity)

    def render(self, stdscr):
        if self.__border:
            stdscr.border(self.__border_color)
        if self.__entities:
            for entity in self.__entities:
                entity.render(stdscr)

"""
Copyright (C) 2023 Austin Choi
All rights reserved.

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
