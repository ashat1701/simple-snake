import ast


class Settings:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            try:
                with open("snake.cfg", "r") as f:
                    cls.__instance.settings = ast.literal_eval(f.read())
            except IOError:
                cls.__instance.settings = {}
                cls.__instance.settings["head_tile"] = "#"
                cls.__instance.settings["tail_tile"] = "="
                cls.__instance.settings["background_tile"] = " "
                cls.__instance.settings["apple_tile"] = "@"
                cls.__instance.settings["update_time"] = 0.1
        return cls.__instance


