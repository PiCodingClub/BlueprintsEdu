class Generator(object):
    DEFINITIONS = {
        "GENERATOR_OPEN": "<<<",
        "GENERATOR_CLOSE": ">>>",
        "GENERATOR": "generated code",
        "SYSTEM_ATTRIBUTE": "variable",
        "SYSTEM_FUNCTION": "function",
        "SYSTEM_IMPORT": "import",  # IMPORT TAG AUTOMATICALLY IMPORTS ALL CHARACTER AND SPRITES
        "SYSTEM_CHARACTER_INIT": "initialize characters",
        "SYSTEM_SPRITE_INIT": "initialize sprites",
        "CHARACTER": "class character",
        "SPRITE": "class sprite",
        "CHARACTER_ATTRIBUTE": "character variable",
        "CHARACTER_FUNCTION": "character function",
        "SPRITE_ATTRIBUTE": "sprite variable",
        "SPRITE_FUNCTION": "sprite function"
    }

    FINDER = "{} {}".format(DEFINITIONS.get("GENERATOR_OPEN"),
                            DEFINITIONS.get("GENERATOR"))

    SYSTEM_ATTR = "{} {} {} {}".format(DEFINITIONS.get("GENERATOR_OPEN"),
                                       DEFINITIONS.get("GENERATOR"),
                                       DEFINITIONS.get("SYSTEM_ATTRIBUTE"),
                                       DEFINITIONS.get("GENERATOR_CLOSE"))

    SYSTEM_IMPORT = "{} {} {} {}".format(DEFINITIONS.get("GENERATOR_OPEN"),
                                         DEFINITIONS.get("GENERATOR"),
                                         DEFINITIONS.get("SYSTEM_IMPORT"),
                                         DEFINITIONS.get("GENERATOR_CLOSE"))

    SYSTEM_INIT_CHARACTER = "{} {} {} {}".format(DEFINITIONS.get("GENERATOR_OPEN"),
                                                 DEFINITIONS.get("GENERATOR"),
                                                 DEFINITIONS.get("SYSTEM_CHARACTER_INIT"),
                                                 DEFINITIONS.get("GENERATOR_CLOSE"))

    SYSTEM_INIT_SPRITE = "{} {} {} {}".format(DEFINITIONS.get("GENERATOR_OPEN"),
                                              DEFINITIONS.get("GENERATOR"),
                                              DEFINITIONS.get("SYSTEM_SPRITE_INIT"),
                                              DEFINITIONS.get("GENERATOR_CLOSE"))

    CHARACTER_ATTR = "{} {} {} {}".format(DEFINITIONS.get("GENERATOR_OPEN"),
                                          DEFINITIONS.get("GENERATOR"),
                                          DEFINITIONS.get("CHARACTER_ATTRIBUTE"),
                                          DEFINITIONS.get("GENERATOR_CLOSE"))

    CHARACTER_CLASS = "{} {} {} {}".format(DEFINITIONS.get("GENERATOR_OPEN"),
                                           DEFINITIONS.get("GENERATOR"),
                                           DEFINITIONS.get("CHARACTER"),
                                           DEFINITIONS.get("GENERATOR_CLOSE"))

    def __new__(cls, *args, **kwargs):
        raise AttributeError("Generator classes cannot be instantiated")

    def __init__(self):
        raise AttributeError("Generator classes cannot be instantiated")
