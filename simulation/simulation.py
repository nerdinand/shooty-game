from typing import Optional

from .agent import Agent
from .human import Human
from .map import Map
from .map_factory import MapFactory
from .player import Player
from .player_collider import PlayerCollider
from .player_factory import PlayerFactory
from .projectile_collider import ProjectileCollider


class Simulation:
    MAX_TICKS = int(
        10 * 60 * 0.5 * 60  # ticks per frame  # FPS  # minutes
    )  # seconds per minute

    def __init__(
        self,
        agent: Optional[Agent] = None,
        with_human: bool = False,
        bot_count: int = 4,
    ) -> None:
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
        self.player_collider = PlayerCollider(self)
        self.projectile_collider = ProjectileCollider(self)

    def tick(self) -> None:
        self.tick_count += 1
        for player in self.players:
            player.tick(self.player_collider, self.projectile_collider)
        self.map.tick()

    def is_over(self) -> bool:
        return (
            self.__is_time_over() or self.__are_players_dead() or self.__is_agent_dead()
        )

    def alive_players_count(self) -> int:
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
