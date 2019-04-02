import display
import gameloop
import config
import control
from game import Game
import logging


def start():
    try:
        display.init()
        control.init()
        gameloop.start()
    finally:
        control.finish()
        display.exit()
        print("Game over! Score - ", Game.GameState().score)


start()
