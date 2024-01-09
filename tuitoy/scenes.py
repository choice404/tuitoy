"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

import curses

class Scene:
    def __init__(self, name):
        """
                Constructor for the Scene object

                Parameters:
                        name (string): The name of the scene
                Returns:
                        None
                        
        """
        self.__name = name
        self.__windows = []

    def get_name(self):
        """
                Returns the name of the scene

                Parameters:
                        None
                Returns:
                        (string): The name of the scene
        """
        return self.__name

    def set_name(self, name):
        """
                Sets the name of the scene

                Parameters:
                        name (string): The new name of the scene
                Returns:
                        None
        """
        self.__name = name

    def add_window(self, window):
        """
                Adds a window to the scene
                    
                Parameters:
                        window (Window): The window to be added
                Returns:
                        None
        """
        self.__windows.append(window)
        
    def remove_window(self, window):
        """
                Removes a window from the scene

                Parameters:
                        window (Window): The window to be removed
                Returns:    
                        None
        """
        self.__windows.remove(window)

    def render(self, stdscr):
        """
                Renders the scene
                    
                Parameters:
                        stdscr (curses.window): The window to render to
                Returns:
                        None
        """
        if self.__windows:
            for window in self.__windows:
                window.render(stdscr)

    def handle_input(self, key):
        """
                Handles input for the scene

                Parameters:
                        key (int): The key that was pressed
                Returns:
                        None
        """
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
