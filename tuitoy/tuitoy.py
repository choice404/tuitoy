"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

# from app import *
# from scenes import *
# from windows import *
import curses
import time

def run(app_func):
    """
            Wraps the curses.wrapper function to allow for the app to be run
                    
            Parameters:
                    app_func (function): The function that will be wrapped by the curses.wrapper function
            Returns:
                    None
    """
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
        self.no_delay = False
        curses.curs_set(0)

    def set_no_delay(self):
        """
                Sets the no delay flag to true

                Parameters:
                        None
                Returns:
                        None
        """
        self.no_delay = True

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
        if self.no_delay:
            self.__stdscr.nodelay(1)
        self.__stdscr.clear()
        current_frame = 0

        while True:
            if self.__windows:
                for window in self.__windows:
                    window.refresh()
            self.__main_window.refresh()
            self.__stdscr.refresh()

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

            if len(self.__scenes) > 0:
                self.__scenes[self.__current_scene].render(self.__stdscr)

            key = self.__stdscr.getch()
            if key == ord('q'):
                break

            if self.__windows:
                for window in self.__windows:
                    window.handle_input(key)
            if len(self.__scenes) > 0:
                self.__scenes[self.__current_scene].handle_input(key)

            if self.no_delay:
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

    def handle_input(self, key):
        """
                Handles user input for the window

                Parameters:
                        None
                Returns:
                        None
        """
        x = 5

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

    def handle_input(self, key):
        """
                Handles user input for the Text_Window

                Parameters:
                        None
                Returns:
                        None
        """
        super().handle_input(key)

if __name__ == '__main__':
    run(create_app)

"""
Copyright (C) 2023 Austin Choi
All rights reserved.

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
