from .obstacle import Obstacle


class Map:
    WALL_THICKNESS = 0.01

    def __init__(self) -> None:
        self.obstacles: list[Obstacle] = []
        self.__add_edge_obstacles()

    def __add_edge_obstacles(self) -> None:
        self.obstacles.append(
            Obstacle.fixed(
                name="left wall", left=0, top=0, width=Map.WALL_THICKNESS, height=1.0
            )
        )
        self.obstacles.append(
            Obstacle.fixed(
                name="top wall", left=0, top=0, width=1.0, height=Map.WALL_THICKNESS
            )
        )
        self.obstacles.append(
            Obstacle.fixed(
                name="right wall",
                left=1.0 - Map.WALL_THICKNESS,
                top=0.0,
                width=Map.WALL_THICKNESS,
                height=1.0,
            )
        )
        self.obstacles.append(
            Obstacle.fixed(
                name="bottom wall",
                left=0.0,
                top=1.0 - Map.WALL_THICKNESS,
                width=1.0,
                height=Map.WALL_THICKNESS,
            )
        )

    def tick(self) -> None:
        pass
