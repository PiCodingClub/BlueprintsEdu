import pygame as pg


class Character(object):

    def __init__(self, pos, size, alive=True):
        self.pos = pos
        self.size = size
        self.alive = alive

    def get_rect(self):
        return pg.Rect(self.pos, self.size)

    def draw(self, display):
        pass

    def events_handler(self, event):
        pass
