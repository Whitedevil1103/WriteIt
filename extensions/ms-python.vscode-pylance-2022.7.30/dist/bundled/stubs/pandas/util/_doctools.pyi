class TablePlotter:
    cell_width = ...
    cell_height = ...
    font_size = ...
    def __init__(
        self, cell_width: float = ..., cell_height: float = ..., font_size: float = ...
    ) -> None: ...
    def plot(self, left, right, labels=..., vertical: bool = ...): ...
