class RenderSettings:
    def __init__(
        self,
        show_bots: bool = True,
        show_map: bool = True,
        show_visibility: bool = False,
    ) -> None:
        self.show_bots = show_bots
        self.show_map = show_map
        self.show_visibility = show_visibility
