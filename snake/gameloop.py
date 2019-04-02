import time
from game import Game
import display
import config
import logging


def step(CurrentGame):
    last_update_time = CurrentGame.GameState().last_update_time
    current_time = time.time()
    passed_time = 0
    if last_update_time is not None:
        passed_time = current_time - last_update_time
    nn_time = config.Settings().settings["update_time"]
    remain_time = nn_time - passed_time
    time.sleep(remain_time)
    CurrentGame.update()
    CurrentGame.GameState().last_update_time = time.time()


def start():
    CurrentGame = Game()
    CurrentGame.spawn_apple()
    while Game.GameState().state == 0:
        step(CurrentGame)
