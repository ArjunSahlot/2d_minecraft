import pygame
import random
from constants import *
from blocks import *
from player import Player


class World:
    mouse_view_factor = 10

    def __init__(self):
        self.view = [0, 0]
        self.player = Player()
        self.blocks = []
        self.seed = None
        self.generate_terrain()
    
    def generate_terrain(self):
        if self.seed is not None:
            random.seed(self.seed)
        
        self.blocks = [Grass(x, 5) for x in range(-18, 18)]

    def update(self, window, events):
        self.player.update(window, self.view, self.blocks)
        for block in self.blocks:
            block.update(window, self.view)
        
        self.update_view()
    
    def update_view(self):
        player_loc = (BLOCK_SIZE * self.player.x, BLOCK_SIZE * self.player.y)
        mouse_loc = pygame.mouse.get_pos() - np.array((WIDTH/2, HEIGHT/2))
        self.view = player_loc + mouse_loc / self.mouse_view_factor
