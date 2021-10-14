import pygame
from pygame.locals import *

KEYS = {
    K_w: pygame.math.Vector2(0, -1), 
    K_a: pygame.math.Vector2(-1, 0), 
    K_s: pygame.math.Vector2(0, 1), 
    K_d: pygame.math.Vector2(1, 0)
}

SCREEN_ORIGIN = pygame.math.Vector2(0, 0)
SCREEN_MAX = pygame.math.Vector2(640, 640)

SCREENRECT = Rect(SCREEN_ORIGIN.x, SCREEN_ORIGIN.y, SCREEN_MAX.x, SCREEN_MAX.y)

BACKGROUND_COLOR = Color(0, 43, 54)
HUMAN_COLOR = Color(38, 139, 210)
BOT_COLOR = Color(220, 50, 47)
GUN_COLOR = Color(101, 123, 131)
OBSTACLES_COLOR = Color(238, 232, 213)
PROJECTILES_COLOR = Color(211, 54, 130)

PLAYER_EXTENT = 0.03
GUN_LENGTH = 15

PLAYER_ACCELERATION = 0.00001
PLAYER_ACCELERATION_DAMPENING = 0.9

MAX_VELOCITY = 1e-4
MAX_VELOCITY_SQUARED = MAX_VELOCITY * MAX_VELOCITY

INITIAL_HEALTH = 100
