import display
import gameloop
import config
import control
import game
import logging


def start():
    try:
        config.init()
        display.init()
        logging.basicConfig(filename="debug.log", level=logging.INFO)
        control.init()
        gameloop.start()
    finally:
        control.finish()
        display.exit()
        print("Game over! Score - ", game.GameState.inst().score)



start()
