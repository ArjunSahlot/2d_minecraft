#
#  2d minecraft
#  2 dimensional minecraft
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import pygame
import os
from constants import *
import numpy as np


class Block:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = pygame.image.load(os.path.join(PARDIR, "blocks", self.img_name + ".png"))
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
    
    def update(self, window, view):
        self.draw(window, view)
    
    def draw(self, window, view):
        loc = (WIDTH/2 + BLOCK_SIZE * self.x, HEIGHT/2 + BLOCK_SIZE * self.y) - np.array(view)

        if loc[0] + BLOCK_SIZE >= 0 and loc[0] <= WIDTH and loc[1] + BLOCK_SIZE >= 0 and loc[1] <= HEIGHT:
            window.blit(self.image, loc)


class Dirt(Block):
    img_name = "dirt"


class Grass(Block):
    img_name = "grass"


class Stone(Block):
    img_name = "stone"
