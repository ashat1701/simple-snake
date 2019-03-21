import curses
import os
import time
import game
import config


class Display:
    __instance = None

    @staticmethod
    def inst():
        if Display.__instance == None:
            Display.__instance = Display()
        return Display.__instance

    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(1)
        try:
            curses.start_color()
        except Exception:
            pass
        self.rows, self.columns = [int(i) for i in os.popen('stty size', 'r').read().split()]
        self.screen.resize(self.rows, self.columns)
        curses.curs_set(0)
        self.screen.border(0)
        self.screen.refresh()


def draw_xy(x, y, sym):
    display = Display.inst()
    display.screen.addstr(y + 1, x + 1, sym)
    display.screen.refresh()

def get_field_size():
    return Display.inst().columns - 2, Display.inst().rows - 2


def draw_snake(snake):
    settings = config.Settings.inst().settings
    draw_xy(snake.head.x, snake.head.y, settings["head_tile"])
    for part in snake.body:
        draw_xy(part.x, part.y, settings["tail_tile"])
    draw_xy(snake.lastPos.x, snake.lastPos.y, settings["background_tile"])


def draw_apples(apples):
    settings = config.Settings.inst().settings
    for apple in apples:
        draw_xy(apple.x, apple.y, settings["apple_tile"])

"""def configure(screen):



    screen.refresh()
    len = 5
    head_x = 10
    head_y = 10
    for body in range(len):
        screen.addch(head_x - body, head_y, "#")
    screen.refresh()
    time.sleep(1)
    while (True):
        screen.addch((rows+head_x - len + 1) % rows, head_y, " ")
        screen.addch((head_x + 1) % rows, head_y, "#")
        screen.refresh()
        head_x+=1
        head_x %= rows

        time.sleep(0.1)

    screen.getch()
"""


def init():
    Display.inst()


def exit():
    Display.inst().screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
