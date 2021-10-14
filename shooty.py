import time
import itertools

import pygame
from pygame.locals import *

from constants import *
from map import Map
from player import Human, Bot
from util import random_vector2

def random_bot():
    return Bot(random_vector2(min=0.1, max=0.8))

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

        if not human.is_dead():
            human_movement_direction = pygame.math.Vector2()
            for k, v in KEYS.items():
                if (keystate[k]):
                    human_movement_direction += v

            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                human.gun.shoot()

        screen.fill(BACKGROUND_COLOR)
        map.draw(screen)

        for player in players:
            if not player.is_dead():
                all_projectiles = list(itertools.chain.from_iterable([p.gun.projectiles for p in set(players) - set([player])])) # flatten
                player.update_projectile_collisions(all_projectiles)

                if player == human:
                    player.update_velocity(human_movement_direction)
                    player.update_direction(mouse_position)
                else:
                    player.gun.shoot()
                    player.randomise_direction()
                    player.randomise_movement_direction()
                    player.update_velocity(player.movement_direction)

                if map.collides_with(player):
                    player.collide()

                for other_player in list(set(players) - set([player])):
                    if not other_player.is_dead() and other_player.collides_with(player):
                        player.collide()
                    
            player.tick(delta)
            player.draw(screen)

        # print(' FPS: ' + str(clock.get_fps()), end='')
        print('', end='\r')

        pygame.display.update()
        delta = clock.tick()


if __name__ == '__main__':
    main()
