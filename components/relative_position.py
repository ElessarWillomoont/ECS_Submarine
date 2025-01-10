class RelativePosition:
    def __init__(self, rel_x, rel_y):
        """
        rel_x: float
            X position relative to the screen width (0.0 ~ 1.0).
        rel_y: float
            Y position relative to the horizon height (-1.0 ~ 1.0).
            -1.0: Below horizon, 1.0: Above horizon.
        """
        self.rel_x = rel_x  # Relative to screen width
        self.rel_y = rel_y  # Relative to horizon height
