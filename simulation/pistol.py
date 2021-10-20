from .gun import Gun

class Pistol(Gun):
  def __init__(self, player):
    super().__init__(player, cooldown_ticks=300, bullet_count=10, damage=75)
