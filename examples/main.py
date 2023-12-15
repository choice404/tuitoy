"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import curses
import time
from tuitoy import entities_old, menu_old, window_old, scenes_old

def main(stdscr):
    game = Game(stdscr)

    game.run()

class Game:
    # Constructor for the game object
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        # self.entities_old = [entities_old.Entity("foo", "foobar", 5, 5, 'X'), entities_old.Entity("bar", "barfoo", 10, 10)]
        self.entities_old = [entities_old.Square(self.stdscr, "", 10, 5, 5)]
        # self.entities_old = [entities_old.Entity(stdscr, "", "", 5, 5, 'X')]
        # self.entities_old = []
        self.window_old = window_old.Window(stdscr)
        self.menu_old = menu_old.Menu(self.window_old, 'x', 'y')
        self.scenes_old = [scenes_old.TitleScene(self.stdscr, "title", self.window_old,
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
        []), scenes_old.Scene(self.stdscr, "foo", self.window_old, [])]
        self.current_scene = self.scenes_old[0]

    # Name: get_window
    # Parameters: self
    # Return: Window self.window_old
    # Description: Returns the window_old object being used by the Game
    def get_window(self):
        return self.window_old

    def get_menu(self):
        return self.menu_old

    def get_entities(self):
        return self.entities_old

    def get_stdscr(self):
        return self.stdscr

    def run(self):

        self.menu_old.menu_arrow_set()
        left, right = self.menu_old.get_direction_keys()
        # i = 0
        # while i < 10:
        #     entity = entities_old.Entity("foo", "foobar", i * 10, self.window_old.get_max_height() - 9, str(i%10))
        #     self.entities_old.append(entity)
        #     i += 1

        # i = 0
        # while i < 10:
        #     entity = entities_old.Entity("foo", "foobar", (self.window_old.get_max_width() - (i * 10) - 1), self.window_old.get_max_height() - 9, str(i%10))
        #     self.entities_old.append(entity)
        #     i += 1
        self.stdscr.clear()

        while True:
            self.menu_old.append_menu_map('test', ["foo", "bar", "foobar", "buzz", "fizz", "tuitoy"]) 
            self.menu_old.append_menu_map('code', ['codedex'])
            self.menu_old.set_menu('test')
            self.menu_old.draw(self.stdscr)
            self.current_scene.draw(self.stdscr)

            for entity in self.entities_old:
                entity.draw()
            
            key = self.stdscr.getch()
            if key == ord('q'):
                break
            # elif key == ord('w'):
            #     self.entities_old[0].move(-1,0, self.window_old)
            # elif key == ord('a'):
            #     self.entities_old[0].move(0,-1, self.window_old)
            # elif key == ord('s'):
            #     self.entities_old[0].move(1,0, self.window_old)
            # elif key == ord('d'):
            #     self.entities_old[0].move(0,1, self.window_old)

            if key in left:
                self.menu_old.move_cursor(-1)
            elif key in right:
                self.menu_old.move_cursor(1)

            # for entity in self.entities_old:
            #     entity.move(1, 0)

            self.stdscr.refresh()
            self.window_old.refresh()
            self.current_scene.refresh()
            self.menu_old.refresh()
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
