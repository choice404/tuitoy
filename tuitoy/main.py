"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""
import curses
import time

# Name: run
# Parameters: (function) app
# Return: None
# Description: Wraps the curses.wrapper function to allow for the app to be run
def run(app_func):
    curses.wrapper(app_func)

class App:
    # Name: __init__
    # Parameters: (curses.window) stdscr
    # Return: None
    # Description: Constructor for the App object
    def __init__(self, stdscr):
        self.__stdscr = stdscr
        self.__scenes = {} 
        self.__windows = []
        self.__current_scene = ""
        self.__fps = 60
        self.__show_fps = False
        curses.curs_set(0)

    # Name: get_fps
    # Parameters: None
    # Return: (int) fps
    # Description: Returns the current fps
    def get_fps(self):
        return self.__fps

    # Name: set_fps
    # Parameters: (int) fps
    # Return: None
    # Description: Sets the current fps
    def set_fps(self, fps):
        self.__fps = fps

    # Name: toggle_fps
    # Parameters: None
    # Return: None
    # Description: Toggles whether or not the fps is shown
    def toggle_fps(self):
        self.__show_fps = not self.__show_fps

    # Name: render
    # Parameters: None
    # Return: None
    # Description: Renders the app
    def render(self):
        self.__stdscr.nodelay(1)
        self.__stdscr.clear()
        current_frame = 0
        while True:
            if self.__show_fps:
                self.__stdscr.addstr(0, 0, "FPS: " + str(current_frame + 1))
                current_frame = (current_frame + 1) % self.__fps

            if self.__windows:
                for window in self.__windows:
                    window.render(self.__stdscr)

            key = self.__stdscr.getch()

            if len(self.__scenes) > 0:
                self.__scenes[self.__current_scene].render(self.__stdscr)
                self.__scenes[self.__current_scene].handle_input(key)

            self.__stdscr.refresh()

            time.sleep(1/self.__fps)

    # Name: add_window
    # Parameters: (Window) window
    # Return: None
    # Description: Adds a window to the list of windows that will always be rendered
    def add_window(self, window):
        self.__windows.append(window)

    # Name: remove_window
    # Parameters: (Window) window
    # Return: None
    # Description: Removes a window from the list of windows that will always be rendered
    def remove_window(self, window):
        self.__windows.remove(window)

    # Name: add_scene
    # Parameters: (string) scene_name, (Scene) scene
    # Return: None
    # Description: Adds a scene to the list of scenes that can be rendered
    def append_scene(self, scene_name, scene):
        self.__scenes[scene_name] = scene

    # Name: remove_scene
    # Parameters: (string) scene_name
    # Return: None
    # Description: Removes a scene from the list of scenes that can be rendered
    def remove_scene(self, scene_name):
        del self.__scenes[scene_name]

    # Name: change_scene
    # Parameters: (string) scene_name
    # Return: None
    # Description: Changes the current scene to the scene with the given name
    def change_scene(self, scene_name):
        self.__current_scene = scene_name

# Name: main
# Parameters: (curses.window) stdscr
# Return: None
# Description: The main function that will be wrapped by the run function to run the app
def main(stdscr):
    app = App(stdscr)
    app.toggle_fps()
    app.render()

if __name__ == '__main__':
    run(main)

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
