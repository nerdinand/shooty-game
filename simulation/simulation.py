from typing import cast
from typing import Optional

from .agent import Agent
from .human import Human
from .map import Map
from .map_factory import MapFactory
from .math_util import MathUtil
from .obstacle import Obstacle
from .player import Player
from .player_collider import PlayerCollider
from .player_factory import PlayerFactory
from .projectile_collider import ProjectileCollider


class Simulation:
    """The main Simulation class of the game. Can be used without a GUI."""

    MAX_TICKS = int(
        10 * 60 * 0.5 * 60  # ticks per frame  # FPS  # minutes
    )  # seconds per minute

    def __init__(
        self,
        seed: Optional[int] = None,
        agent: Optional[Agent] = None,
        with_human: bool = False,
        bot_count: int = 4,
    ) -> None:
        """Initialize a new Simulation.

        Arguments:
           seed (optional, int): Seed for the random number generator.
           agent (optional, Agent): An AI Agent that interacts with the simulation.
           with_human (optional, bool): Whether to spawn a human player or not.
           bot_count (optional, int): The number of bots to spawn in the simulation.
        """
        MathUtil.seed(seed)

        player_factory = PlayerFactory()
        self.players: list[Player] = []
        self.human: Optional[Human] = None

        for _i in range(bot_count):
            self.players.append(player_factory.random_bot())

        if with_human:
            self.human = player_factory.human()
            self.players.append(self.human)

        self.agent = agent
        if not self.agent is None:
            self.players.append(self.agent)

        self.map: Map = MapFactory.simple_map()
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
