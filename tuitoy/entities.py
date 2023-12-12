"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

class Entity:
    def __init__(self, stdscr, name, description, x=0, y=0, char = '0'):
        self.__stdscr = stdscr
        self.__name = name
        self.__desc = description
        self.__x = x
        self.__y = y
        self.__char = char

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def set_name(self, name):
        self.__name = name

    def set_desc(self, description):
        self.__desc = description

    def check_collision(self, window):
        if self.__x >= window.max_width - 1:
            self.__x = window.max_width - 1
        if self.__y >= window.max_height - 1:
            self.__y = window.max_height - 1
        if self.__x <= 0:
            self.__x = 0
        if self.__y <= 0:
            self.__y = 0

    def move(self, dx, dy, window):
        self.__y += dy
        self.__x += dx
        self.check_collision(window)
    
    def draw(self):
        self.__stdscr.addch(self.__y, self.__x, self.__char)

class Shape:
    def __init__(self, stdscr, x=0, y=0):
        self.__stdscr = stdscr
        self.__x = x
        self.__y = y

class Square(Shape):
    def __init__(self, stdscr, text="", length=1, x=0, y=0):
        super().__init__(stdscr, x, y)
        self.__length = length
        self.__text = text

    def draw(self, stdscr):
        horizontal = ('-' * self.__length) + '-' + '-'

        stdscr.addstr(self._Shape__y, self._Shape__x, horizontal)
        stdscr.addstr(self._Shape__y + self.__length + 1, self._Shape__x, horizontal)
        for i in range (self.__length):
            stdscr.addch(self._Shape__y + i + 1, self._Shape__x, '|')
            stdscr.addch(self._Shape__y + i + 1, self._Shape__x + self.__length + 1, '|')

        # super().__stdscr.addstr(super().__y, super().__x, horizontal)
        # super().__stdscr.addstr(super().__y + self.__length, super().__x, horizontal)
        # for i in range (self.__length - 2):
        #     super().__stdscr.addch(super().__y + i + 1, super().__x, '|')
        #     super().__stdscr.addch(super().__y + i + 1, super().__x + self.__length, '|')

def main():
  # Enter code here
  print("entities.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
