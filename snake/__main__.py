import display
import keyboard
import gameloop
import config


def start():
    try:
        config.init()
        display.init()
        keyboard.init()
        gameloop.start()
    finally:
        display.exit()


start()
