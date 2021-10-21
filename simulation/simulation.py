from .player_factory import PlayerFactory
from .map_factory import MapFactory
from .player_collider import PlayerCollider
from .projectile_collider import ProjectileCollider

class Simulation:
  MAX_TICKS = ( 10 # ticks per frame
            * 60 # FPS
            * 2 # minutes
            * 60 ) # seconds per minute

  def __init__(self):
    player_factory = PlayerFactory()
    self.human = player_factory.human()
    self.players = [
      self.human,
      player_factory.random_bot(),
      player_factory.random_bot(),
      player_factory.random_bot(),
      player_factory.random_bot()
    ]
    map_factory = MapFactory()
    self.map = map_factory.simple_map()
    self.tick_count = 0
    self.player_collider = PlayerCollider(self)
    self.projectile_collider = ProjectileCollider(self)

  def tick(self):
    self.tick_count += 1
    for player in self.players:
      player.tick(self.player_collider, self.projectile_collider)
    self.map.tick()

  def is_over(self):
    return self.__is_time_over() or self.__are_players_dead()

  def alive_players_count(self):
    return sum(map(lambda p: not p.is_dead, self.players))

  def __is_time_over(self):
    return self.tick_count >= Simulation.MAX_TICKS

  def __are_players_dead(self):
    return self.alive_players_count() <= 1 and len(self.players) > 1

def main():
  pass

if __name__ == '__main__':
  main()
