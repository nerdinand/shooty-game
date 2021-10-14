import pygame
from pygame.locals import *

from constants import *

class Map:
    def __init__(self):
        self.screen_obstacles = []
        self.__add_edge_obstacles()

    def collides_with(self, entity):
        return entity.screen_rect().collidelist(self.screen_obstacles) != -1

    def __add_edge_obstacles(self):
        wall_thickness = 0.01
        self.add_obstacle(0.0, 0.0, wall_thickness, 1.0) # left wall
        self.add_obstacle(0.0, 0.0, 1.0, wall_thickness) # top wall
        self.add_obstacle(1.0 - wall_thickness, 0.0, wall_thickness, 1.0) # right wall
        self.add_obstacle(0.0, 1.0 - wall_thickness, 1.0, wall_thickness) # bottom wall

    def add_obstacle(self, left, top, width, height):
        self.screen_obstacles.append(Obstacle(left, top, width, height).screen_rect())

    def draw(self, screen):
        for screen_obstacle in self.screen_obstacles:
            pygame.draw.rect(screen, OBSTACLES_COLOR, screen_obstacle)

class Obstacle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def screen_rect(self):
        return Rect(
            self.left * SCREEN_MAX[0],
            self.top * SCREEN_MAX[1],
            self.width * SCREEN_MAX[0],
            self.height * SCREEN_MAX[1]
        )
