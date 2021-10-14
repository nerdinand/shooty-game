import random

import pygame

from constants import *


def to_screen_position(position):
    return position.elementwise() * SCREEN_MAX

def to_game_position(screen_position):
    return pygame.math.Vector2(screen_position).elementwise() / SCREEN_MAX

def random_vector2(min=0.0, max=1.0):
    return pygame.math.Vector2(random.uniform(min, max), random.uniform(min, max))

def random_direction_change():
    return random.uniform(-10.0, 10.0)
