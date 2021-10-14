import pygame

from util import to_screen_position, to_game_position

from constants import *
from geometry import calculateIntersectPoint


class Gun:
    def __init__(self, player):
        self.player = player
        self.shooting = False
        self.cooldown_ticks = 200
        self.ticks_elapsed = 0
        self.projectiles = []

    def tick(self, delta):
        if self.shooting:
            self.ticks_elapsed += delta

        if self.ticks_elapsed >= self.cooldown_ticks:
            self.shooting = False
            self.ticks_elapsed = 0

        for projectile in self.projectiles:
            projectile.tick(delta)
            if projectile.is_dead():
                self.projectiles.remove(projectile)

    def shoot(self):
        if self.shooting:
            return None
        self.shooting = True
        self.projectiles.append(Projectile(self.player.position, self.player.direction))

    def draw(self, screen):
        screen_position = to_screen_position(self.player.position)
        pygame.draw.line(screen, GUN_COLOR, screen_position, screen_position + self.gun_tip())
        for projectile in self.projectiles:
            projectile.draw(screen)

    def gun_tip(self):
        v = pygame.math.Vector2()
        v.from_polar((GUN_LENGTH, self.player.direction))
        return v

class Projectile:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        v = pygame.math.Vector2()
        v.from_polar((GUN_LENGTH, self.direction))
        self.screen_from = to_screen_position(self.position) + v
        self.screen_to = self.screen_from + 10 * v
        self.ticks_to_live = 200
        self.ticks_alive = 0
        self.dead = False

    def tick(self, delta):
        self.ticks_alive += delta
        self.dead = self.dead or self.ticks_alive > self.ticks_to_live

    def is_dead(self):
        return self.dead

    def draw(self, screen):
        pygame.draw.line(screen, PROJECTILES_COLOR, self.screen_from, self.screen_to)

    def collides_with(self, rect):
        top_line = ((rect.left, rect.top), (rect.left+rect.width, rect.top))
        right_line = ((rect.left+rect.width, rect.top), (rect.left+rect.width, rect.top+rect.height))
        bottom_line = ((rect.left, rect.top+rect.height), (rect.left+rect.width, rect.top+rect.height))
        left_line  = ((rect.left, rect.top), (rect.left, rect.top+rect.height))

        for line in [top_line, right_line, bottom_line, left_line]:
            if calculateIntersectPoint(self.screen_from, self.screen_to, line[0], line[1]) != None:
                return True

        return False

    def die(self):
        self.dead = True