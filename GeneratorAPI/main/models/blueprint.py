from utils import logger_utils
from utils.enums.status import Status


class Blueprint(object):

    def __init__(self, name, b_type):
        self.name = name
        self.type = b_type

    def to_dict(self):
        return {
            "NAME": self.name,
            "TYPE": self.type
        }

    def __str__(self):
        return "{} = {}".format(self.name, str(None))


class AttributeBlueprint(Blueprint):

    def __init__(self, name=Status.NONE, b_type=Status.NONE, data_type=Status.NONE, value=Status.NONE):
        Blueprint.__init__(self, name, b_type)
        self.__logger = logger_utils.get_logger(__name__)
        self.data_type = data_type
        self.value = value

    def to_dict(self):
        r = super().to_dict()
        r["DATA"] = {
            "TYPE": self.data_type,
            "VALUE": self.value
        }
        return r

    def __str__(self):
        if self.data_type == "string" or self.data_type == "char":
            return "{} = '{}'".format(self.name.lower(), self.value)
        else:
            return "{} = {}".format(self.name.lower(), self.value)


class CharacterBlueprint(Blueprint):

    def __init__(self, name=Status.NONE, b_type=Status.NONE, pos=None, size=None, alive=True, attributes=None, functions=None,
                 sprites=None):
        Blueprint.__init__(self, name, b_type)
        if pos is None:
            self.pos = (0, 0)
        else:
            self.pos = pos
        if size is None:
            self.size = (0, 0)
        else:
            self.size = size
        self.alive = alive
        if attributes is None:
            self.attributes = list()
        else:
            self.attributes = attributes
        if functions is None:
            self.functions = list()
        else:
            self.functions = functions
        if sprites is None:
            self.sprites = list()
        else:
            self.sprites = sprites

    def to_dict(self):
        r = super().to_dict()
        r["POSITION"] = self.pos
        r["SIZE"] = self.size
        r["ALIVE"] = self.alive
        lb = list()
        for b in self.attributes:
            lb.append(b.to_dict())
        r["ATTRIBUTES"] = lb
        lb = list()
        for b in self.functions:
            lb.append(b.to_dict())
        r["FUNCTIONS"] = lb
        for b in self.sprites:
            lb.append(b.to_dict())
        r["SPRITES"] = lb
        return r

    def __str__(self):
        return "{}Character".format(self.name)


class FunctionBlueprint(Blueprint):

    def __init__(self, name=Status.NONE, b_type=Status.NONE, code=None):
        Blueprint.__init__(self, name, b_type)
        self.code = code

    def to_dict(self):
        r = super().to_dict()
        r["CODE"] = self.code
        return r


class SpriteBlueprint(Blueprint):

    def __init__(self, name=Status.NONE, b_type=Status.NONE, attributes=None, functions=None):
        Blueprint.__init__(self, name, b_type)
        if attributes is None:
            self.attributes = list()
        else:
            self.attributes = attributes
        if functions is None:
            self.functions = list()
        else:
            self.functions = functions

    def to_dict(self):
        r = super().to_dict()
        lb = list()
        for b in self.attributes:
            lb.append(b.to_dict())
        r["ATTRIBUTES"] = lb
        lb = list()
        for b in self.functions:
            lb.append(b.to_dict())
        r["FUNCTIONS"] = lb
        return r
