from player import Player

import pygame

class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}