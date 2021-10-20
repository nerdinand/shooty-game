import pygame
from pygame.math import Vector2

class PlayerCollider:
  def __init__(self, simulation):
    self.simulation = simulation

  def move(self, player):
    dx = player.velocity.x
    dy = player.velocity.y

    if dx != 0:
        self.__move_single_axis(player, dx, 0)
    if dy != 0:
        self.__move_single_axis(player, 0, dy)

  def __move_single_axis(self, player, dx, dy):
    # Move the rect
    player.position.x += dx
    player.position.y += dy

    for obstacle in self.simulation.map.obstacles:
      self.__adjust_for_collision(player, obstacle, dx, dy)

    for other_player in self.simulation.players:
      if player == other_player or other_player.is_dead: # can't collide with myself or with dead players
        continue
      self.__adjust_for_collision(player, other_player.bounding_box(), dx, dy)

  def __adjust_for_collision(self, player, obstacle, dx, dy):
    player_radius = player.radius()

    if self.__does_collide(player.bounding_box(), obstacle):
      if dx > 0: # Moving right; Hit the left side of the obstacle
        player.position.x = obstacle.left() - player_radius
      if dx < 0: # Moving left; Hit the right side of the obstacle
        player.position.x = obstacle.right() + player_radius
      if dy > 0: # Moving down; Hit the top side of the obstacle
        player.position.y = obstacle.top() - player_radius
      if dy < 0: # Moving up; Hit the bottom side of the obstacle
        player.position.y = obstacle.bottom() + player_radius

  def __does_collide(self, player_obstacle, map_obstacle):
    return (
      player_obstacle.left() < map_obstacle.left() + map_obstacle.width and
      player_obstacle.left() + player_obstacle.width > map_obstacle.left() and
      player_obstacle.top() < map_obstacle.top() + map_obstacle.height and
      player_obstacle.height + player_obstacle.top() > map_obstacle.top()
    )