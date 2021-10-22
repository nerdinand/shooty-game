from .bot import Bot
from .human import Human
from .math_util import MathUtil
from .pistol import Pistol
from .rifle import Rifle


class PlayerFactory:
  def __init__(self) -> None:
    pass

  def random_bot(self) -> Bot:
    return Bot(gun=Rifle, position=MathUtil.random_vector2(min=0.1, max=0.8))

  def human(self) -> Human:
    return Human(gun=Pistol)
