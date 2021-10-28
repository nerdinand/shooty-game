from .bot import Bot
from .human import Human
from .math_util import MathUtil
from .pistol import Pistol
from .rifle import Rifle


class PlayerFactory:
  def __init__(self) -> None:
    self.bot_count = 0

  def random_bot(self) -> Bot:
    bot = Bot(
      f'Bot {self.bot_count}',
      gun=Rifle,
      position=MathUtil.random_vector2(min=0.1, max=0.8)
    )
    self.bot_count += 1
    return bot

  def human(self) -> Human:
    return Human('Human', gun=Rifle)
