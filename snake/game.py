import display
import random


class GameObject:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)


class Snake:
    def __init__(self):
        self.body = []
        self.head = GameObject()
        self.lastPos = GameObject()


class GameState:
    __instance = None

    @staticmethod
    def inst():
        if GameState.__instance == None:
            GameState.__instance = GameState()
        return GameState.__instance

    def __init__(self):
        self.snake = Snake()
        self.apples = []
        self.direction = (1, 0)
        self.score = 0
        self.grow = 0
        self.last_update_time = None
        self.state = 0
        self.listener = None


def update():
    check_apple()
    snake_move()
    check_position()
    display.draw_snake(GameState.inst().snake)
    display.draw_apples(GameState.inst().apples)


def init():
    spawn_apple()


def spawn_apple():
    width, height = display.get_field_size()
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    new_apple = GameObject(x, y)
    if new_apple in GameState.inst().apples or new_apple == GameState.inst().snake.head or new_apple in GameState.inst().snake.body:
        spawn_apple()
    else:
        GameState.inst().apples.append(new_apple)


def eat_apple(i):
    GameState.inst().apples.pop(i)
    spawn_apple()
    GameState.inst().grow += 1
    GameState.inst().score += 1


def check_apple():
    for i, apple in enumerate(GameState.inst().apples):
        if GameState.inst().snake.head == apple:
            eat_apple(i)


def snake_move():
    previous_part = None
    snake = GameState.inst().snake
    full_snake = [snake.head] + snake.body
    snake.lastPos = GameObject(full_snake[-1].x, full_snake[-1].y)
    previous_part = GameObject(snake.head.x, snake.head.y)
    snake.head.x += GameState.inst().direction[0]
    snake.head.y += GameState.inst().direction[1]
    for i, part in enumerate(snake.body):
        new_x = previous_part.x
        new_y = previous_part.y
        previous_part = GameObject(part.x, part.y)
        part.x = new_x
        part.y = new_y
    if GameState.inst().grow > 0:
        snake.body.append(previous_part)
        GameState.inst().grow -= 1


def update_direction(direction):
    negate = (-i for i in direction)
    if negate != GameState.inst().direction:
        GameState.inst().direction = direction


def check_boundaries(obj):
    width, height = display.get_field_size()
    return 0 <= obj.x < width and 0 <= obj.y < height


def check_position():
    if GameState.inst().snake.head in GameState.inst().snake.body or not check_boundaries(GameState.inst().snake.head):
        GameState.inst().state = 1
