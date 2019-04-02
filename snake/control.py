from pynput import keyboard
from game import Game


def on_press(key):
    controls = {keyboard.Key.down: (0, 1), keyboard.Key.up: (0, -1), keyboard.Key.left: (-1, 0), keyboard.Key.right: (1, 0)}
    if key in controls:
        Game.update_direction(controls[key])


def init():
    Game.GameState().listener = keyboard.Listener(on_press=on_press)
    Game.GameState().listener.start()


def finish():
    Game.GameState().listener.stop()
