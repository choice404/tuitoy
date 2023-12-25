import scenes, windows, main

def Main(stdscr):
    app = main.App(stdscr)
    app.add_window(windows.Window(10, 10, 10, 10, True))
    app.add_window(windows.Window(20, 20, 20, 20, True))
    app.toggle_border()
    app.toggle_fps()
    main.create_app(app)

if __name__ == '__main__':
    main.run(Main)
