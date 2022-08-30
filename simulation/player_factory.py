from .agent import Agent
from .bot import Bot
from .configuration import BotConfiguration
from .human import Human
from .math_util import MathUtil
from .rifle import Rifle
from .simple_bot import SimpleBot
from .static_bot import StaticBot


class PlayerFactory:
    def __init__(self) -> None:
        self.bot_count = 0

    def bot(self, bot_configuration: BotConfiguration) -> Bot:
        bot = None

        match bot_configuration.kind:
            case "SimpleBot":  # TODO: constant
                bot = self.__simple_bot()
            case "StaticBot":  # TODO: constant
                bot = self.__static_bot()
            case _:
                raise ValueError(
                    f"'{bot_configuration.kind}' is not a valid kind of bot."
                )

        if bot is not None:
            self.bot_count += 1

        return bot

    def human(self) -> Human:
        return Human("Human", gun_class=Rifle)

    def agent(self) -> Agent:
        return Agent("Agent", gun_class=Rifle)

    def __simple_bot(self) -> Bot:
        return SimpleBot(
            f"SimpleBot {self.bot_count}",
            gun_class=Rifle,
            position=MathUtil.random_vector2(minimum=0.1, maximum=0.8),
        )

    def __static_bot(self) -> Bot:
        return StaticBot(
            f"StaticBot {self.bot_count}",
            gun_class=Rifle,
            position=MathUtil.random_vector2(minimum=0.1, maximum=0.8),
        )
