"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import curses
import time
from tuitoy import entities, menu, window, scenes

def main(stdscr):
    game = Game(stdscr)

    game.run()

class Game:
    # Constructor for the game object
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        # self.entities = [entities.Entity("foo", "foobar", 5, 5, 'X'), entities.Entity("bar", "barfoo", 10, 10)]
        # self.entities = [entities.Square(self.stdscr, "", 10, 5, 5)]
        self.entities = []
        self.window = window.Window(stdscr)
        self.menu = menu.Menu(self.window)
        self.scenes = [scenes.TitleScene(self.stdscr, "title", self.window,
        """        ,----,                            ,----,                         
      ,/   .`|                          ,/   .`|  ,----..                
    ,`   .'  :               ,---,    ,`   .'  : /   /   \\               
  ;    ;     /       ,--, ,`--.' |  ;    ;     //   .     :        ,---, 
.'___,/    ,'      ,'_ /| |   :  :.'___,/    ,'.   /   ;.  \\      /_ ./| 
|    :     |  .--. |  | : :   |  '|    :     |.   ;   /  ` ;,---, |  ' : 
;    |.';  ;,'_ /| :  . | |   :  |;    |.';  ;;   |  ; \\ ; /___/ \\.  : | 
`----'  |  ||  ' | |  . . '   '  ;`----'  |  ||   :  | ; | '.  \\  \\ ,' ' 
    '   :  ;|  | ' |  | | |   |  |    '   :  ;.   |  ' ' ' : \\  ;  `  ,' 
    |   |  ':  | | :  ' ; '   :  ;    |   |  ''   ;  \\; /  |  \\  \\    '  
    '   :  ||  ; ' |  | ' |   |  '    '   :  | \\   \\  ',  /    '  \\   |  
    ;   |.' :  | : ;  ; | '   :  |    ;   |.'   ;   :    /      \\  ;  ;  
    '---'   '  :  `--'   \\;   |.'     '---'      \\   \\ .'        :  \\  \\ 
            :  ,      .-./'---'                   `---`           \\  ' ; 
             `--`----'                                             `--`  
                                                                         """,
        []), scenes.Scene(self.stdscr, "foo", self.window, [])]
        self.current_scene = self.scenes[0]

    # Name: get_window
    # Parameters: self
    # Return: Window self.window
    # Description: Returns the window object being used by the Game
    def get_window(self):
        return self.window

    def get_menu(self):
        return self.menu

    def get_entities(self):
        return self.entities

    def get_stdscr(self):
        return self.stdscr

    def run(self):

        self.menu.menu_arrow_set()
        left, right = self.menu.get_direction_keys()
        # i = 0
        # while i < 10:
        #     entity = entities.Entity("foo", "foobar", i * 10, self.window.get_max_height() - 9, str(i%10))
        #     self.entities.append(entity)
        #     i += 1

        # i = 0
        # while i < 10:
        #     entity = entities.Entity("foo", "foobar", (self.window.get_max_width() - (i * 10) - 1), self.window.get_max_height() - 9, str(i%10))
        #     self.entities.append(entity)
        #     i += 1

        while True:
            self.stdscr.clear()
            self.menu.append_menu_map('test', ["foo", "bar", "foobar", "buzz", "fizz", "tuitoy"]) 
            self.menu.set_menu('test')
            self.menu.draw(self.stdscr)
            self.current_scene.draw(self.stdscr)

            for entity in self.entities:
                entity.draw(self.stdscr)
            
            key = self.stdscr.getch()
            if key == ord('q'):
                break

            if key in left:
                self.menu.move_cursor(-1)
            elif key in right:
                self.menu.move_cursor(1)

            # for entity in self.entities:
            #     entity.move(1, 0)

            self.stdscr.refresh()
            self.window.refresh()
            self.current_scene.refresh()
            self.menu.refresh()
            time.sleep(1/120)

if __name__ == '__main__':
    curses.wrapper(main)

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
