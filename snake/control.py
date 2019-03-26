from pynput import keyboard
import game


def on_press(key):
    controls = {keyboard.Key.down: (0, 1), keyboard.Key.up: (0, -1), keyboard.Key.left: (-1, 0), keyboard.Key.right: (1, 0)}
    if key in controls:
        game.update_direction(controls[key])


def init():
    game.GameState.inst().listener = keyboard.Listener(on_press=on_press)
    game.GameState.inst().listener.start()


def finish():
    game.GameState.inst().listener.stop()
