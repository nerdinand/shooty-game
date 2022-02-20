from .obstacle import Obstacle


class Map:
    WALL_THICKNESS = 0.01

    def __init__(self) -> None:
        self.obstacles: list[Obstacle] = []
        self.__add_edge_obstacles()

    def __add_edge_obstacles(self) -> None:
        self.obstacles.append(Obstacle("left wall", 0, 0, Map.WALL_THICKNESS, 1.0))
        self.obstacles.append(Obstacle("top wall", 0, 0, 1.0, Map.WALL_THICKNESS))
        self.obstacles.append(
            Obstacle(
                "right wall", 1.0 - Map.WALL_THICKNESS, 0.0, Map.WALL_THICKNESS, 1.0
            )
        )
        self.obstacles.append(
            Obstacle(
                "bottom wall", 0.0, 1.0 - Map.WALL_THICKNESS, 1.0, Map.WALL_THICKNESS
            )
        )

    def tick(self) -> None:
        pass
