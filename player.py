import pygame
from pygame.locals import *

from constants import *
from gun import Gun
from util import to_screen_position, to_game_position, random_direction_change, random_vector2

class Player:
    def __init__(self, position):
        self.position = position
        self.velocity = pygame.math.Vector2(0.0, 0.0)
        self.direction = 0.0
        self.collision_position = None
        self.gun = Gun(self)
        self.health = INITIAL_HEALTH

    def update_direction(self, mouse_position):
        self.direction = (to_game_position(mouse_position) - self.position).as_polar()[1]

    def update_velocity(self, direction):
        if direction == pygame.math.Vector2(0.0, 0.0):
            self.velocity *= PLAYER_ACCELERATION_DAMPENING
        else:
            self.velocity += direction * PLAYER_ACCELERATION

        if self.velocity.length_squared() > MAX_VELOCITY_SQUARED:
            self.velocity.scale_to_length(MAX_VELOCITY)

    def tick(self, delta):
        if not self.is_dead():
            self.__update_position(delta)

        self.gun.tick(delta)

    def __update_position(self, delta):
        self.position += self.velocity * delta

    def collide(self):
        if self.collision_position == None:
            self.collision_position = self.position
            
        self.position = self.collision_position
        self.velocity = -self.velocity

    def uncollide(self):
        self.collision_position = None

    def draw(self, screen):
        screen_rect = self.screen_rect()
        pygame.draw.ellipse(screen, self.color, screen_rect, width=1)

        if self.is_dead():
            pygame.draw.line(screen, self.color, (screen_rect.left, screen_rect.top), (screen_rect.right, screen_rect.bottom))
            pygame.draw.line(screen, self.color, (screen_rect.left, screen_rect.bottom), (screen_rect.right, screen_rect.top))

        self.gun.draw(screen)

    def screen_rect(self):
        player_screen_extent = SCREEN_MAX * PLAYER_EXTENT
        left_top = to_screen_position(self.position) - (player_screen_extent / 2.0)
        return Rect(left_top.x, left_top.y, player_screen_extent.x, player_screen_extent.y)

    def collides_with(self, entity):
        return entity.screen_rect().colliderect(self.screen_rect())

    def is_dead(self):
        return self.health <= 0

    def remove_health(self, amount):
        self.health -= amount
        if self.is_dead():
            self.die()

    def die(self):
        self.velocity = pygame.math.Vector2(0.0, 0.0)

    def update_projectile_collisions(self, projectiles):
        screen_rect = self.screen_rect()
        colliding_projectiles = [p for p in projectiles if p.collides_with(screen_rect)]

        for colliding_projectile in colliding_projectiles:
            self.remove_health(10)
            colliding_projectile.die()

class Bot(Player):
    def __init__(self, position=pygame.math.Vector2(0.5, 0.5)):
        self.color = BOT_COLOR
        self.movement_direction = pygame.math.Vector2()
        super().__init__(position)

    def randomise_movement_direction(self):
        self.movement_direction += random_vector2(min=-1.0, max=1.0)

    def randomise_direction(self):
        self.direction += random_direction_change()

    def collide(self):
        self.movement_direction = pygame.math.Vector2(0.0, 0.0)
        super().collide()

    def die(self):
        self.movement_direction = pygame.math.Vector2(0.0, 0.0)
        super().die()

class Human(Player):
    def __init__(self, position=pygame.math.Vector2(0.5, 0.5)):
        self.color = HUMAN_COLOR
        super().__init__(position)
