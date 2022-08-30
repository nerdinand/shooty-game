from typing import cast
from typing import Optional

from .agent import Agent
from .bot import Bot
from .configuration import Configuration
from .human import Human
from .map import Map
from .map_factory import MapFactory
from .math_util import MathUtil
from .obstacle import Obstacle
from .player import Player
from .player_collider import PlayerCollider
from .player_factory import PlayerFactory
from .projectile_collider import ProjectileCollider


class Simulation:  # pylint: disable=too-many-instance-attributes
    """The main Simulation class of the game. Can be used without a GUI."""

    MAX_TICKS = int(
        10 * 60 * 0.5 * 60  # ticks per frame  # FPS  # minutes
    )  # seconds per minute

    def __init__(
        self, configuration: Configuration, agent: Optional[Agent] = None
    ) -> None:
        """Initialize a new Simulation."""
        MathUtil.seed(configuration.random_seed)

        player_factory = PlayerFactory()
        self.players: list[Player] = []
        self.bots: list[Bot] = []
        self.human: Optional[Human] = None

        for bot_configuration in configuration.bots:
            bot = player_factory.bot(bot_configuration)
            self.bots.append(bot)
            self.players.append(bot)

        if configuration.with_human:
            self.human = player_factory.human()
            self.players.append(self.human)

        self.agent = agent
        if not self.agent is None:
            self.players.append(self.agent)

        self.map: Map = MapFactory.map(configuration.map)
        self.tick_count = 0
        self.player_collider = PlayerCollider(self.get_obstacles())
        self.projectile_collider = ProjectileCollider(self.get_obstacles())

    def tick(self) -> None:
        """Simulate a single "tick" (quantum of time)."""
        self.tick_count += 1
        for player in self.players:
            player.tick(self.player_collider, self.projectile_collider)
        self.map.tick()

    def get_obstacles(self) -> list[Obstacle]:
        """Return the obstacles in the simulation (including map and players)."""
        return self.map.obstacles + cast(list[Obstacle], self.players)

    def is_over(self) -> bool:
        """Return whether the simulation is over."""
        return (
            self.__is_time_over() or self.__are_players_dead() or self.__is_agent_dead()
        )

    def dead_bots_count(self) -> int:
        return sum(map(lambda p: p.is_dead, self.bots))

    def alive_players_count(self) -> int:
        """Return how many players are alive in the simulation."""
        return sum(map(lambda p: not p.is_dead, self.players))

    def __is_time_over(self) -> bool:
        return self.tick_count >= Simulation.MAX_TICKS

    def __are_players_dead(self) -> bool:
        return (
            self.alive_players_count() <= 1  # pylint: disable=chained-comparison
            and len(self.players) > 1
        )

    def __is_agent_dead(self) -> bool:
        if self.agent is None:
            return False

        return self.agent.is_dead
