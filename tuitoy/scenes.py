"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

import curses

class Scene:
    # Name: __init__
    # Parameters: (string) name
    # Return: None
    # Description: Constructor for the Scene object
    def __init__(self, name):
        self.__name = name
        self.__windows = []

    # Name: get_name
    # Parameters: None
    # Return: (string) name
    # Description: Returns the name of the scene
    def get_name(self):
        return self.__name

    # Name: set_name
    # Parameters: (string) name
    # Return: None
    # Description: Sets the name of the scene
    def set_name(self, name):
        self.__name = name

    # Name: add_window
    # Parameters: (Window) window   
    # Return: None
    # Description: Adds a window to the scene
    def add_window(self, window):
        self.__windows.append(window)
        
    # Name: remove_window
    # Parameters: (Window) window
    # Return: None
    # Description: Removes a window from the scene
    def remove_window(self, window):
        self.__windows.remove(window)

    # Name: render
    # Parameters: (curses.window) stdscr
    # Return: None
    # Description: Renders the scene
    def render(self, stdscr):
        if self.__windows:
            for window in self.__windows:
                window.render(stdscr)

    # Name: handle_input
    # Parameters: (int) key
    # Return: None
    # Description: Handles input for the scene
    def handle_input(self, key):
        if self.__windows:
            for window in self.__windows:
                window.handle_input(key)

"""
Copyright (C) 2023 Austin Choi
All rights reserved.

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
