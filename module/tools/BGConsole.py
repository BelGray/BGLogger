import enum
import random


class BGC:

    __version__ = "1.1.0"
    __github__ = "https://github.com/BelGray/BGConsole.py"

    class Color(enum.Enum):
        PINK = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        RED = "\033[31m"
        GREEN = '\033[92m'
        MUSTARD = '\033[93m'
        CRIMSON = '\033[91m'
        YELLOW = '\033[33m'
        PURPLE = "\033[35m"
        BLACK = "\033[30m"
        WHITE = "\033[37m"
        NULL = ""

    class Param(enum.Enum):
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        NULL = ""

    class Tool(enum.Enum):
        EMPTY = ""
        OFF = '\033[0m'
        NULL = ""

    @staticmethod
    def random_color() -> Color:
        return random.choice(list(BGC.Color))

    @staticmethod
    def random_param() -> Param:
        return random.choice(list(BGC.Param))

    @staticmethod
    def write(text: str, param: Param = None, color: Color = None):
        OFF = '\033[0m'
        if param == None:
            param = BGC.Param.NULL
        if color == None:
            color = BGC.Color.NULL

        print(OFF + str(param.value) + str(color.value) + str(text) + OFF)
        return OFF + str(param.value) + str(color.value) + str(text) + OFF

    @staticmethod
    def scan(label: str, label_param: Param = None, label_color: Color = None, input_text_param: Param = None,
             input_text_color: Color = None):
        OFF = '\033[0m'
        if label == None:
            label = ""
        if label_color == None:
            label_color = BGC.Color.NULL
        if input_text_color == None:
            input_text_color = BGC.Color.NULL
        if label_param == None:
            label_param = BGC.Param.NULL
        if input_text_param == None:
            input_text_param = BGC.Param.NULL

        return str(input(OFF + str(label_param.value) + str(label_color.value) + str(label) + OFF + str(input_text_param.value) + str(input_text_color.value)))