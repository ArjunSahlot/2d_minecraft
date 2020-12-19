import pygame
import random
from constants import *
from blocks import *
# from player import Player


class World:
    def __init__(self):
        self.view = [0, 0]
        # self.player = Player()
        self.blocks = []
        self.seed = None
        self.generate_terrain()
    
    def generate_terrain(self):
        if self.seed is not None:
            random.seed(self.seed)
        
        self.blocks = [Dirt(18, y) for y in range(-18, 18)]

    def update(self, window, events):
        self.player.update(window, self.view, events, self.blocks)
        for block in self.blocks:
            block.update(window, self.view)
        
        self.update_view()
    
    def update_view(self):
        pass