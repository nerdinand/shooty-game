from .bot import Bot
from .human import Human
from .math_util import MathUtil

class PlayerFactory:
  def __init__(self):
    pass

  def random_bot(self):
    return Bot(MathUtil.random_vector2(min=0.1, max=0.8))

  def human(self):
    return Human()
