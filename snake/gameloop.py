import time
import game
import display
import config
import logging

def step():
    last_update_time = game.GameState.inst().last_update_time
    current_time = time.time()
    passed_time = 0
    if last_update_time is not None:
        passed_time = current_time - last_update_time
    nn_time = config.Settings.inst().settings["update_time"]
    remain_time = nn_time - passed_time
    time.sleep(remain_time)
    logging.info("Update time {}. State - {}".format(time.time(), game.GameState.inst().state))
    game.update()
    game.GameState.inst().last_update_time = time.time()


def init():
    game.init()


def start():
    init()
    while game.GameState.inst().state == 0:
        step()
