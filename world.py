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
