from pynput import mouse


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def init():
    listener = mouse.Listener(on_press=on_press)
    listener.start()
