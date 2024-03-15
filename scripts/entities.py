import pygame

class physicsEntity:
    def __init__(self, game, entityType, pos, size):
        self.game = game
        self.type = entityType
        self.pos = list(pos)