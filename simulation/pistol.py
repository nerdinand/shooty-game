from .gun import Gun
from .spray_pattern import SprayPattern

class Pistol(Gun):
  def __init__(self, player):
    super().__init__(
      player, 
      cooldown_ticks=300,
      reload_ticks=500,
      magazine_size=10,
      damage=75,
      spray_pattern=SprayPattern([
        0,
        -0.8292242732279771,
        -0.7574842949823672,
        0.7016835732931053,
        -0.8244637468978553,
        -0.11310783710790218,
        -0.48438163674411006,
        0.5448335084111124,
        0.9629322493363133,
        0.22640097004334403
      ])
    )
