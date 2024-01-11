"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""
from tuitoy import tuitoy

def main(stdscr):
    my_app = tuitoy.App(stdscr)

    max_height, max_width = stdscr.getmaxyx()

    my_app.set_no_delay()

    my_app.add_window(tuitoy.Text_Window(0, 0, max_width, max_height, True, [
"        ,----,                            ,----,                         ",
"      ,/   .`|                          ,/   .`|  ,----..                ",
"    ,`   .'  :               ,---,    ,`   .'  : /   /   \\               ",
"  ;    ;     /       ,--, ,`--.' |  ;    ;     //   .     :        ,---, ",
".'___,/    ,'      ,'_ /| |   :  :.'___,/    ,'.   /   ;.  \\      /_ ./| ",
"|    :     |  .--. |  | : :   |  '|    :     |.   ;   /  ` ;,---, |  ' : ",
";    |.';  ;,'_ /| :  . | |   :  |;    |.';  ;;   |  ; \\ ; /___/ \\.  : | ",
"`----'  |  ||  ' | |  . . '   '  ;`----'  |  ||   :  | ; | '.  \\  \\ ,' ' ",
"    '   :  ;|  | ' |  | | |   |  |    '   :  ;.   |  ' ' ' : \\  ;  `  ,' ",
"    |   |  ':  | | :  ' ; '   :  ;    |   |  ''   ;  \\; /  |  \\  \\    '  ",
"    '   :  ||  ; ' |  | ' |   |  '    '   :  | \\   \\  ',  /    '  \\   |  ",
"    ;   |.' :  | : ;  ; | '   :  |    ;   |.'   ;   :    /      \\  ;  ;  ",
"    '---'   '  :  `--'   \\;   |.'     '---'      \\   \\ .'        :  \\  \\ ",
"            :  ,      .-./'---'                   `---`           \\  ' ; ",
"             `--`----'                                             `--`  ",
"",
"",
"By Austin Choi",
        ],
        'center'
    ))

    tuitoy.create_app(my_app)

if __name__ == '__main__':
    tuitoy.run(main)

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
