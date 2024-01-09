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
    def __init__(self, stdscr):
        """
                Constructor for the App object

                Parameters:
                        stdscr (curses.window): The main window that is passed in from the curses.wrapper function
                Returns:
                        None
                        
        """
        self.__stdscr = stdscr
        self.__scenes = {} 
        self.__windows = []
        self.__current_scene = ""
        self.__fps = 60
        self.__show_fps = False
        self.__border = False
        self.__main_window = curses.newwin(0, 0, 0, 0)
        curses.curs_set(0)

    def get_fps(self):
        """
                Returns the current fps

                Parameters:
                        None
                Returns:
                        (int): The current fps
        """
        return self.__fps

    def set_fps(self, fps):
        """
                Sets the current fps

                Parameters:
                        fps (int): The new fps
                Returns:
                        None
        """
        self.__fps = fps

    def toggle_fps(self):
        """
                Toggles whether or not the fps is shown

                Parameters:
                        None
                Returns:
                        None
        """
        self.__show_fps = not self.__show_fps
    
    def toggle_border(self):
        """
                Toggles whether or not the border is shown

                Parameters:
                        None
                Returns:
                        None
        """
        self.__border = not self.__border

    def render(self):
        """
                Renders the app

                Parameters:
                        None
                Returns:
                        None
        """
        self.__stdscr.nodelay(1)
        self.__stdscr.clear()
        current_frame = 0
        while True:
            if self.__show_fps:
                if self.__border:
                    self.__stdscr.addstr(1, 1, "FPS: " + str(current_frame + 1))
                else:
                    self.__stdscr.addstr(0, 0, "FPS: " + str(current_frame + 1))
                current_frame = (current_frame + 1) % self.__fps

            if self.__windows:
                for window in self.__windows:
                    window.render(self.__stdscr)

            if self.__border:
                self.__main_window.border()

            key = self.__stdscr.getch()
            if len(self.__scenes) > 0:
                self.__scenes[self.__current_scene].render(self.__stdscr)
                self.__scenes[self.__current_scene].handle_input(key)

            self.__stdscr.refresh()
            self.__main_window.refresh()
            for window in self.__windows:
                window.refresh()

            time.sleep(1/self.__fps)

    def add_window(self, window):
        """
                Adds a window to the list of windows that will always be rendered

                Parameters:
                        window (Window): The window to be added
                Returns:
                        None
        """
        self.__windows.append(window)

    def remove_window(self, window):
        """
                Removes a window from the list of windows that will always be rendered

                Parameters:
                        window (Window): The window to be removed
                Returns:
                        None
        """
        self.__windows.remove(window)

    def append_scene(self, scene_name, scene):
        """
                Adds a scene to the list of scenes that can be rendered

                Parameters:
                        scene_name (string): The name of the scene
                        scene (Scene): The scene to be added
                Returns:
                        None
        """
        self.__scenes[scene_name] = scene

    def remove_scene(self, scene_name):
        """
                Removes a scene from the list of scenes that can be rendered

                Parameters:
                        scene_name (string): The name of the scene
                Returns:
                        None
        """
        del self.__scenes[scene_name]

    def change_scene(self, scene_name):
        """
                Changes the current scene to the scene with the given name

                Parameters:
                        scene_name (string): The name of the scene
                Returns:
                        None
        """
        self.__current_scene = scene_name

def create_app(app):
    """
            The main function that will be wrapped by the run function to run the app

            Parameters:
                    app (App): The app to be run
            Returns:
                    None
    """
    app.render()

if __name__ == '__main__':
    run(create_app)

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
