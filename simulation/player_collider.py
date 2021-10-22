from __future__ import annotations  # to allow for forward type references
from typing import TYPE_CHECKING

import pygame
from pygame.math import Vector2

from .rectangle import Rectangle
if TYPE_CHECKING:
  from .simulation import Simulation
  from .player import Player


class PlayerCollider:
  def __init__(self, simulation: Simulation):
    self.simulation = simulation

  def move(self, player: Player) -> None:
    dx = player.velocity.x
    dy = player.velocity.y

    if dx != 0:
        self.__move_single_axis(player, dx, 0)
    if dy != 0:
        self.__move_single_axis(player, 0, dy)

  def __move_single_axis(self, player: Player, dx: float, dy: float) -> None:
    # Move the rect
    player.position.x += dx
    player.position.y += dy

    for obstacle in self.simulation.map.obstacles:
      self.__adjust_for_collision(player, obstacle.get_rectangle(), dx, dy)

    for other_player in self.simulation.players:
      # can't collide with myself or with dead players
      if player == other_player or other_player.is_dead:
        continue
      self.__adjust_for_collision(player, other_player.get_rectangle(), dx, dy)

  def __adjust_for_collision(
    self, player: Player, rectangle: Rectangle, dx: float, dy: float
  ) -> None:
    player_radius = player.radius()

    if self.__does_collide(player.get_rectangle(), rectangle):
      if dx > 0:  # Moving right; Hit the left side of the obstacle
        player.position.x = rectangle.left() - player_radius
      if dx < 0:  # Moving left; Hit the right side of the obstacle
        player.position.x = rectangle.right() + player_radius
      if dy > 0:  # Moving down; Hit the top side of the obstacle
        player.position.y = rectangle.top() - player_radius
      if dy < 0:  # Moving up; Hit the bottom side of the obstacle
        player.position.y = rectangle.bottom() + player_radius

  def __does_collide(self, player_rectangle: Rectangle, map_rectangle: Rectangle) -> bool:
    return (
      player_rectangle.left() < map_rectangle.left() + map_rectangle.width and
      player_rectangle.left() + player_rectangle.width > map_rectangle.left() and
      player_rectangle.top() < map_rectangle.top() + map_rectangle.height and
      player_rectangle.height + player_rectangle.top() > map_rectangle.top()
    )
