from utils.utils import Utils
from utils.string_utils import StringUtils
from pygame.locals import *
import pygame as pg

CAPTION = "BlueprintEdu V1.0"

# FRAMES PER SECOND
FPS = 90


class GeneratorError(Exception):
    """Description: Special error definition for generator exceptions"""


class ResponseParsingError(Exception):
    """Description: Special error definition for JSON parsing exceptions"""


class DownloadError(Exception):
    """Description: Special error definition to project download exception"""


class Events(Utils):
    SPECIAL_KEYS = {
        "DELETE": "DEL",
        "BACKSPACE": "BACK",
        "UNREGISTERED": "UNKNOWN",
    }

    UPPERCASE = False

    @classmethod
    def get_char(cls, key, event_type=KEYUP):
        if key == K_a:
            if Events.UPPERCASE:
                return "A"
            else:
                return "a"
        elif key == K_b:
            if Events.UPPERCASE:
                return "B"
            else:
                return "b"
        elif key == K_c:
            if Events.UPPERCASE:
                return "C"
            else:
                return "c"
        elif key == K_d:
            if Events.UPPERCASE:
                return "D"
            else:
                return "d"
        elif key == K_e:
            if Events.UPPERCASE:
                return "E"
            else:
                return "e"
        elif key == K_f:
            if Events.UPPERCASE:
                return "F"
            else:
                return "f"
        elif key == K_g:
            if Events.UPPERCASE:
                return "G"
            else:
                return "g"
        elif key == K_h:
            if Events.UPPERCASE:
                return "H"
            else:
                return "h"
        elif key == K_i:
            if Events.UPPERCASE:
                return "I"
            else:
                return "i"
        elif key == K_j:
            if Events.UPPERCASE:
                return "J"
            else:
                return "j"
        elif key == K_k:
            if Events.UPPERCASE:
                return "K"
            else:
                return "k"
        elif key == K_l:
            if Events.UPPERCASE:
                return "L"
            else:
                return "l"
        elif key == K_m:
            if Events.UPPERCASE:
                return "M"
            else:
                return "m"
        elif key == K_n:
            if Events.UPPERCASE:
                return "N"
            else:
                return "n"
        elif key == K_o:
            if Events.UPPERCASE:
                return "O"
            else:
                return "o"
        elif key == K_p:
            if Events.UPPERCASE:
                return "P"
            else:
                return "p"
        elif key == K_q:
            if Events.UPPERCASE:
                return "Q"
            else:
                return "q"
        elif key == K_r:
            if Events.UPPERCASE:
                return "R"
            else:
                return "r"
        elif key == K_s:
            if Events.UPPERCASE:
                return "S"
            else:
                return "s"
        elif key == K_t:
            if Events.UPPERCASE:
                return "T"
            else:
                return "t"
        elif key == K_u:
            if Events.UPPERCASE:
                return "U"
            else:
                return "u"
        elif key == K_v:
            if Events.UPPERCASE:
                return "V"
            else:
                return "v"
        elif key == K_w:
            if Events.UPPERCASE:
                return "W"
            else:
                return "w"
        elif key == K_x:
            if Events.UPPERCASE:
                return "X"
            else:
                return "x"
        elif key == K_y:
            if Events.UPPERCASE:
                return "Y"
            else:
                return "y"
        elif key == K_z:
            if Events.UPPERCASE:
                return "Z"
            else:
                return "z"
        elif key == K_0 or key == K_KP0:
            if Events.UPPERCASE and key == K_0:
                return ")"
            else:
                return "0"
        elif key == K_1 or key == K_KP1:
            return "1"
        elif key == K_2 or key == K_KP2:
            return "2"
        elif key == K_3 or key == K_KP3:
            return "3"
        elif key == K_4 or key == K_KP4:
            return "4"
        elif key == K_5 or key == K_KP5:
            return "5"
        elif key == K_6 or key == K_KP6:
            return "6"
        elif key == K_7 or key == K_KP7:
            return "7"
        elif key == K_8 or key == K_KP8:
            return "8"
        elif key == K_9 or key == K_KP9:
            if Events.UPPERCASE and key == K_9:
                return "("
            else:
                return "9"
        elif key == K_DELETE:
            return Events.SPECIAL_KEYS.get("DELETE")
        elif key == K_BACKSPACE:
            return Events.SPECIAL_KEYS.get("BACKSPACE")
        elif key == K_SPACE:
            return " "
        elif key == K_LSHIFT or key == K_RSHIFT:

            if event_type == KEYDOWN:
                Events.UPPERCASE = True
            elif event_type == KEYUP:
                Events.UPPERCASE = False
        elif key == K_KP_PERIOD:
            return "."
        elif key == K_COMMA:
            return ","
        else:
            return Events.SPECIAL_KEYS.get("UNREGISTERED")


class DisplaySettings(Utils):

    SCREEN_SIZES = {
        "800x600": [800, 600],
        "1024x720": [1024, 720],
        "1024x768": [1024, 768],
        "1280x720": [1280, 720],
        "1280x800": [1280, 800],
        "1280x960": [1280, 960],
        "1280x1024": [1280, 1024]
    }

    DEFAULT_SCREEN_SIZE = SCREEN_SIZES.get("800x600")

    @classmethod
    def get_size_by_key(cls, key=None):
        if key is None:
            return DisplaySettings.DEFAULT_SCREEN_SIZE
        else:
            return DisplaySettings.SCREEN_SIZES.get(key)

    @classmethod
    def get_size_name(cls, size=None):
        r = None
        if size is None:
            size = DisplaySettings.DEFAULT_SCREEN_SIZE
        for k, v in DisplaySettings.SCREEN_SIZES.items():
            if v == size:
                r = k
        return r

    @classmethod
    def get_size_by_id(cls, size_id):
        r = None
        i = 0
        for k, v in DisplaySettings.SCREEN_SIZES.items():
            if i == size_id:
                r = v
                break
            i += 1
        return r

    @classmethod
    def set_size_by_key(cls, key):
        DisplaySettings.DEFAULT_SCREEN_SIZE = DisplaySettings.get_size_by_key(key)


class Colors(Utils):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    DIM_GREY = (105, 105, 105)
    GREY = (128, 128, 128)
    DARK_GREY = (169, 169, 169)
    SILVER = (192, 192, 192)
    VAMPIRE_GREY = (64, 64, 64)
    NIGHT_GREY = (28, 28, 28)
    LIGHT_GREY = (211, 211, 211)
    GAINSBORO = (220, 220, 220)
    WHITE_SMOKE = (245, 245, 245)
    SLATE_GREY = (112, 128, 144)
    LIGHT_SLATE_GREY = (119, 136, 153)
    DARK_ORANGE = (255, 140, 0)
    RANGE_RED = (255, 69, 0)
    DEEP_SKY_BLUE = (0, 191, 255)
    LIGHT_CYAN = (224, 255, 255)
    PALE_TURQUOISE = (175, 238, 238)
    POWDER_BLUE = (176, 224, 230)
    LIGHT_BLUE = (173, 216, 230)
    LAVENDER = (230, 230, 250)
    ALICE_BLUE = (240, 248, 255)
    SNOW = (255, 250, 250)
    ORCHID = (218, 112, 214)
    HOT_PINK = (255, 105, 180)
    PALE_VIOLET_RED = (218, 112, 147)
    VIOLET = (238, 130, 238)
    PURPLE = (128, 0, 128)
    MAGENTA = (255, 0, 255)
    DEEP_PINK = (255, 20, 147)
    LIGHT_PINK = (255, 182, 193)
    PINK = (255, 192, 203)
    MEDIUM_ORCHID = (186, 85, 211)


class Fonts(Utils):
    ROOT_PATH = "resources/fonts/"
    ARCHISTICO_SIMPLE = ROOT_PATH + "Archistico_Simple.ttf"
    ARCHISTICO_BOLD = ROOT_PATH + "Archistico_Bold.ttf"
    SANSATION_BOLD = ROOT_PATH + "Sansation_Bold.ttf"
    SANSATION_BOLDITALIC = ROOT_PATH + "Sansation_BoldItalic.ttf"
    SANSATION_ITALIC = ROOT_PATH + "Sansation_Italic.ttf"
    SANSATION_LIGHT = ROOT_PATH + "Sansation_Light.ttf"
    SANSATION_LIGHTITALIC = ROOT_PATH + "Sansation_LightItalic.ttf"
    SANSATION_REGULAR = ROOT_PATH + "Sansation_Regular.ttf"


class Images(Utils):
    ROOT_PATH = "resources/images/"
    UNDO = ROOT_PATH + "undo.png"
    DROP_DOWN = ROOT_PATH + "drop-down.png"

    @classmethod
    def get_icon(cls, image):
        img = pg.image.load(image)
        img_rect = img.get_rect()
        return img, img_rect


class GameApi(Utils):
    APIS = [
        ["CAR_SIMULATOR_API", StringUtils.get_string("ID_CAR_SIMULATOR")]
    ]
    DEFAULT_API = None

    @staticmethod
    def get_api(id):
        return GameApi.APIS[id]
