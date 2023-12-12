"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

class Window:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.max_height, self.max_width = self.stdscr.getmaxyx()
        self.per_height = self.max_height // 100
        self.per_width = self.max_width // 100

    def get_stdscr(self):
        return self.stdscr

    def get_max_height(self):
        return self.max_height

    def get_max_width(self):
        return self.max_width

    def get_per_height(self):
        return self.per_height

    def get_per_width(self):
        return self.per_width

    def refresh(self):
        self.max_height, self.max_width = self.stdscr.getmaxyx()
        self.per_height = self.max_height // 100
        self.per_width = self.max_width // 100


def main():
  # Enter code here
  print("window.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
