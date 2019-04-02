import display
import random


class Game:
    class GameObject:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __eq__(self, other):
            return (self.x == other.x) and (self.y == other.y)

    class Snake:
        def __init__(self):
            self.body = []
            self.head = Game.GameObject()
            self.lastPos = Game.GameObject()

    class GameState:
        __instance = None

        def __new__(cls):
            if cls.__instance is None:
                cls.__instance = super(Game.GameState, cls).__new__(cls)
                cls.__instance.snake = Game.Snake()
                cls.__instance.apples = []
                cls.__instance.direction = (1, 0)
                cls.__instance.score = 0
                cls.__instance.grow = 0
                cls.__instance.last_update_time = None
                cls.__instance.state = 0
                cls.__instance.listener = None
            return cls.__instance

    def update(self):
        self.check_apple()
        self.snake_move()
        self.check_position()
        display.draw_snake(Game.GameState().snake)
        display.draw_apples(Game.GameState().apples)

    def init(self):
        self.spawn_apple()

    def spawn_apple(self):
        width, height = display.get_field_size()
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        new_apple = self.GameObject(x, y)
        if new_apple in Game.GameState().apples or new_apple == Game.GameState().snake.head or new_apple in Game.GameState().snake.body:
            self.spawn_apple()
        else:
            Game.GameState().apples.append(new_apple)

    def eat_apple(self, i):
        Game.GameState().apples.pop(i)
        self.spawn_apple()
        Game.GameState().grow += 1
        Game.GameState().score += 1

    def check_apple(self):
        for i, apple in enumerate(Game.GameState().apples):
            if Game.GameState().snake.head == apple:
                self.eat_apple(i)

    def snake_move(self):
        previous_part = None
        snake = Game.GameState().snake
        full_snake = [snake.head] + snake.body
        snake.lastPos = self.GameObject(full_snake[-1].x, full_snake[-1].y)
        previous_part = self.GameObject(snake.head.x, snake.head.y)
        snake.head.x += Game.GameState().direction[0]
        snake.head.y += Game.GameState().direction[1]
        for i, part in enumerate(snake.body):
            new_x = previous_part.x
            new_y = previous_part.y
            previous_part = self.GameObject(part.x, part.y)
            part.x = new_x
            part.y = new_y
        if Game.GameState().grow > 0:
            snake.body.append(previous_part)
            Game.GameState().grow -= 1

    def update_direction(direction):
        negate = (-i for i in direction)
        if negate != Game.GameState().direction:
            Game.GameState().direction = direction

    def check_boundaries(obj):
        width, height = display.get_field_size()
        return 0 <= obj.x < width and 0 <= obj.y < height

    def check_position(self):
        if Game.GameState().snake.head in Game.GameState().snake.body or not Game.check_boundaries(
                Game.GameState().snake.head):
            Game.GameState().state = 1
