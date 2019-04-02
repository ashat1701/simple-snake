import curses
import os
import time
import game
import config


class Display:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.screen = curses.initscr()
            curses.noecho()
            curses.cbreak()
            cls.__instance.screen.keypad(1)
            try:
                curses.start_color()
            except Exception:
                pass
            cls.__instance.rows, cls.__instance.columns = [int(i) for i in os.popen('stty size', 'r').read().split()]
            cls.__instance.screen.resize(cls.__instance.rows, cls.__instance.columns)
            curses.curs_set(0)
            cls.__instance.screen.border(0)
            cls.__instance.screen.refresh()
        return cls.__instance


def draw_xy(x, y, sym):
    display = Display()
    display.screen.addstr(y + 1, x + 1, sym)
    display.screen.refresh()


def get_field_size():
    return Display().columns - 2, Display().rows - 2


def draw_snake(snake):
    settings = config.Settings().settings
    draw_xy(snake.head.x, snake.head.y, settings["head_tile"])
    for part in snake.body:
        draw_xy(part.x, part.y, settings["tail_tile"])
    draw_xy(snake.lastPos.x, snake.lastPos.y, settings["background_tile"])


def draw_apples(apples):
    settings = config.Settings().settings
    for apple in apples:
        draw_xy(apple.x, apple.y, settings["apple_tile"])


def init():
    Display()


def exit():
    Display().screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
