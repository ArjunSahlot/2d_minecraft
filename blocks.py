import pygame
import os
from constants import *
import numpy as np


class Block:
    def __init__(self, row, col):
        self.row, self.col = row, col
        self.image = pygame.image.load(os.path.join(PARDIR, "blocks", self.img_name + ".png"))
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
    
    def update(self, window, view):
        self.draw(window, view)
    
    def draw(self, window, view):
        loc = (WIDTH/2 + BLOCK_SIZE * self.col, HEIGHT/2 + BLOCK_SIZE * self.row) + np.array(view)

        if loc[0] > 0 and loc[0] + BLOCK_SIZE < WIDTH and loc[1] > 0 and loc[1] + BLOCK_SIZE < HEIGHT:
            window.blit(self.image, loc)


class Dirt(Block):
    img_name = "dirt"

class Stone(Block):
    img_name = "stone"
