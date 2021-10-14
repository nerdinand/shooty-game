import time
import random

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

PROJECTILE_VELOCITY = 1e-2

def to_screen_position(position):
    return position.elementwise() * SCREEN_MAX

def to_game_position(screen_position):
    return pygame.math.Vector2(screen_position).elementwise() / SCREEN_MAX

def random_vector2(min=0.0, max=1.0):
    return pygame.math.Vector2(random.uniform(min, max), random.uniform(min, max))

def random_bot():
    return Bot(random_vector2(min=0.1, max=0.8))

class Player:
    def __init__(self, position):
        self.position = position
        self.velocity = pygame.math.Vector2(0.0, 0.0)
        self.direction = 0.0
        self.collision_position = None
        self.gun = Gun(self)

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
        pygame.draw.ellipse(screen, self.color, self.screen_rect(), width=1)
        self.gun.draw(screen)

    def screen_rect(self):
        player_screen_extent = SCREEN_MAX * PLAYER_EXTENT
        left_top = to_screen_position(self.position) - (player_screen_extent / 2.0)
        return Rect(left_top.x, left_top.y, player_screen_extent.x, player_screen_extent.y)

    def collides_with(self, entity):
        return entity.screen_rect().colliderect(self.screen_rect())

class Bot(Player):
    def __init__(self, position=pygame.math.Vector2(0.5, 0.5)):
        self.color = BOT_COLOR
        self.movement_direction = pygame.math.Vector2()
        super().__init__(position)

    def randomise_movement_direction(self):
        self.movement_direction += random_vector2(min=-1.0, max=1.0)

    def collide(self):
        self.movement_direction = pygame.math.Vector2(0.0, 0.0)
        super().collide()

class Human(Player):
    def __init__(self, position=pygame.math.Vector2(0.5, 0.5)):
        self.color = HUMAN_COLOR
        super().__init__(position)

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
            if projectile.should_die():
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

    def tick(self, delta):
        self.ticks_alive += delta

    def should_die(self):
        return self.ticks_alive > self.ticks_to_live

    def draw(self, screen):
        pygame.draw.line(screen, PROJECTILES_COLOR, self.screen_from, self.screen_to)

def main():
    pygame.init() # TODO: only initialise what's necessary

    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.mouse.set_visible(False)
    clock =  pygame.time.Clock()

    human = Human()
    players = [human, random_bot(), random_bot(), random_bot(), random_bot()]
    map = Map()
    map.add_obstacle(0.1, 0.1, 0.05, 0.05)
    map.add_obstacle(0.1, 0.7, 0.05, 0.2)
    map.add_obstacle(0.7, 0.1, 0.2, 0.05)
    map.add_obstacle(0.85, 0.85, 0.05, 0.05)
    delta = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return

        keystate = pygame.key.get_pressed()
        mouse_position = pygame.mouse.get_pos()

        human_movement_direction = pygame.math.Vector2()
        for k, v in KEYS.items():
            if (keystate[k]):
                human_movement_direction += v

        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            projectile = human.gun.shoot()

        screen.fill(BACKGROUND_COLOR)
        map.draw(screen)

        for player in players:
            if player == human:
                player.update_velocity(human_movement_direction)
                player.update_direction(mouse_position)
            else:
                player.randomise_movement_direction()
                player.update_velocity(player.movement_direction)

            if map.collides_with(player):
                player.collide()
            else:
                player.uncollide()

            for other_player in list(set(players) - set([player])):
                if other_player.collides_with(player):
                    player.collide()
                else:
                    player.uncollide()

            player.tick(delta)
            player.draw(screen)

        # print(' FPS: ' + str(clock.get_fps()), end='')
        print('', end='\r')

        pygame.display.update()
        delta = clock.tick()


if __name__ == '__main__':
    main()
