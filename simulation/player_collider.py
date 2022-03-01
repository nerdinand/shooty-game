from .obstacle import Obstacle
from .player import Player
from .rectangle import Rectangle


class PlayerCollider:
    def __init__(self, obstacles: list[Obstacle]) -> None:
        self.obstacles = obstacles

    def move(self, player: Player) -> None:
        dx = player.velocity.x  # pylint: disable=invalid-name
        dy = player.velocity.y  # pylint: disable=invalid-name

        if dx != 0:
            self.__move_single_axis(player, dx, 0)
        if dy != 0:
            self.__move_single_axis(player, 0, dy)

    def __move_single_axis(
        self, player: Player, dx: float, dy: float  # pylint: disable=invalid-name
    ) -> None:
        # Move the rect
        player.position.x += dx
        player.position.y += dy

        for obstacle in self.obstacles:
            if isinstance(obstacle, Player):
                other_player: Player = obstacle
                # can't collide with myself or with dead players
                if player == other_player or other_player.is_dead:
                    continue

            PlayerCollider.__adjust_for_collision(
                player, obstacle.get_rectangle(), dx, dy
            )

    @classmethod
    def __adjust_for_collision(
        cls,
        player: Player,
        rectangle: Rectangle,
        dx: float,  # pylint: disable=invalid-name
        dy: float,  # pylint: disable=invalid-name
    ) -> None:
        player_radius = player.radius

        if PlayerCollider.__does_collide(player.get_rectangle(), rectangle):
            if dx > 0:  # Moving right; Hit the left side of the obstacle
                player.position.x = rectangle.left() - player_radius
            if dx < 0:  # Moving left; Hit the right side of the obstacle
                player.position.x = rectangle.right() + player_radius
            if dy > 0:  # Moving down; Hit the top side of the obstacle
                player.position.y = rectangle.top() - player_radius
            if dy < 0:  # Moving up; Hit the bottom side of the obstacle
                player.position.y = rectangle.bottom() + player_radius

    @classmethod
    def __does_collide(
        cls, player_rectangle: Rectangle, map_rectangle: Rectangle
    ) -> bool:
        return (
            player_rectangle.left() < map_rectangle.left() + map_rectangle.width
            and player_rectangle.left() + player_rectangle.width > map_rectangle.left()
            and player_rectangle.top() < map_rectangle.top() + map_rectangle.height
            and player_rectangle.height + player_rectangle.top() > map_rectangle.top()
        )
