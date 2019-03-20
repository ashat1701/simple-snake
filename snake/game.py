class ScreenObject:
    def __init__(self):
        self.x = 0
        self.y = 0


class Snake:
    def __init__(self):
        self.body = []
        self.head = ScreenObject()
        self.lastPos = ScreenObject()

