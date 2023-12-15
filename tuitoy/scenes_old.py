"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

import curses

class Scene:
    def __init__(self, stdscr, name, window, entities=[]):
        self.__stdscr = stdscr
        self.__name = name
        self.__window = window
        self.__entities = entities
        self.__width = self.__window.max_width - (10 * self.__window.per_width)
        self.__height = self.__window.max_height - 10
        self.__x = 4 * self.__window.per_width
        self.__y = 1
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def draw(self, stdscr):
        horizontal = ('-' * self.__width) + '-' + '-'

        stdscr.addstr(self.__y, self.__x, horizontal)
        stdscr.addstr(self.__y + self.__height + 1, self.__x, horizontal)
        for i in range (self.__height):
            stdscr.addch(self.__y + i + 1, self.__x, '|')
            stdscr.addch(self.__y + i + 1, self.__x + self.__width + 1, '|')

    def refresh(self):
        self.__width = self.__window.max_width - (10 * self.__window.per_width)
        self.__height = self.__window.max_height - 10
        self.__x = 4 * self.__window.per_width
        self.__y = 1


class TitleScene(Scene):
    def __init__(self, stdscr, name, window, title, entities=[]):
        super().__init__(stdscr, name, window, entities)
        self.__title = title.split('\n')
        self.__title_length = len(self.__title)

    def draw(self, stdscr):
        super().draw(stdscr)
        for i, line in enumerate(self.__title):
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(10 + i, (self._Scene__window.max_width - 87) //2, line)
            stdscr.attroff(curses.color_pair(1))

def main():
  # Enter code here
  print("scenes.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
