import pygame

from .input import KeyMapper, DirectionMapper, MouseHandler
from .renderer import Renderer

class Gui:
  def __init__(self, render_every_tick_count = 10, key_target_player = None, resolution = (800, 600)):
    self.tick_count = 0
    self.render_every_tick_count = render_every_tick_count
    self.key_target_player = key_target_player
    self.key_mapper = KeyMapper()
    self.direction_mapper = DirectionMapper()
    self.renderer = Renderer(resolution)
    self.mouse_handler = MouseHandler(self.renderer.screen_rect)

  def initialize(self):
    pygame.init() # TODO: only initialise what's necessary

    self.renderer.initialize()
    self.clock =  pygame.time.Clock()

  def tick(self):
    self.tick_count += 1

  def render(self, simulation):
    self.renderer.render(simulation)
    self.tick_count = 0

  def handle_key_events(self):
    if self.key_target_player is None:
      return
    directions = self.key_mapper.map()
    if KeyMapper.QUIT in directions:
      return
    direction_vector = self.direction_mapper.map(directions)
    self.key_target_player.update_move_direction(direction_vector)

  def handle_mouse_events(self):
    if self.key_target_player is None:
      return
    self.mouse_handler.handle_mouse_events(self.key_target_player)

  def should_quit(self):
    return KeyMapper.QUIT in self.key_mapper.map()

  def is_render_necessary(self):
    return self.tick_count == self.render_every_tick_count