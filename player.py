import pygame
from constants import *
import numpy as np


class Player:
    width, height = 0.8, 1.8
    max_vel = 8
    acceleration = .4
    deceleration = .6

    def __init__(self):
        self.x = self.y = 0
        self.vel_x = self.vel_y = 0
    
    def update(self, window, view, blocks):
        self.draw(window, view)

        self.x += self.vel_x / FPS
        self.y += self.vel_y / FPS

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = max(self.vel_x - self.acceleration, -self.max_vel)
        elif keys[pygame.K_RIGHT]:
            self.vel_x = min(self.vel_x + self.acceleration, self.max_vel)
        else:
            self.vel_x -= (self.vel_x and (-1, 1)[self.vel_x > 0]) * (min(abs(self.vel_x), 0.5))
    
    def draw(self, window, view):
        loc = (WIDTH/2 + BLOCK_SIZE * self.x, HEIGHT/2 + BLOCK_SIZE * self.y) - np.array(view)
        pygame.draw.rect(window, WHITE, (*loc, self.width*BLOCK_SIZE, self.height*BLOCK_SIZE))
