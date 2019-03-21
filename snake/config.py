import ast


class Settings:
    __instance = None

    @staticmethod
    def inst():
        if Settings.__instance is None:
            Settings.__instance = Settings()
        return Settings.__instance

    def __init__(self):
        try:
            with open("snake.cfg", "r") as f:
                self.settings = ast.literal_eval(f.read())
        except IOError:
            self.settings = {}
            self.settings["head_tile"] = "#"
            self.settings["tail_tile"] = "="
            self.settings["background_tile"] = " "
            self.settings["apple_tile"] = "@"
            self.settings["update_time"] = 0.1

def init():
    set = Settings.inst()

