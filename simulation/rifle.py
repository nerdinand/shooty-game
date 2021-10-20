from .gun import Gun

class Rifle(Gun):
  def __init__(self, player):
    super().__init__(player, cooldown_ticks=115, bullet_count=30)
