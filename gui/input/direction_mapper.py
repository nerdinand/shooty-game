from pygame.math import Vector2

from .key_mapper import KeyMapper


class DirectionMapper:
    """Maps key events to directions in 2 dimensional game space."""

    DIRECTIONS: dict[str, Vector2] = {
        KeyMapper.UP: Vector2(0, -1),
        KeyMapper.LEFT: Vector2(-1, 0),
        KeyMapper.DOWN: Vector2(0, 1),
        KeyMapper.RIGHT: Vector2(1, 0),
    }

    @classmethod
    def map(cls, key_events: list[str]) -> Vector2:
        """Map key events to directions."""
        direction_vector = Vector2()
        for key_event in key_events:  # pylint: disable=not-an-iterable
            if key_event in DirectionMapper.DIRECTIONS:
                direction_vector += DirectionMapper.DIRECTIONS[key_event]

        if direction_vector.length_squared() != 0.0:
            direction_vector.normalize_ip()

        return direction_vector
