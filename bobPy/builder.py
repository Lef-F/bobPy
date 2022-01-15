import numpy as np
from dataclasses import dataclass, field
from typing import List


@dataclass
class Plank:
    """A plank is born.
    Please use integer millimeters for dimensions.
    """

    width: int
    length: int
    height: int

    def __post_init__(self) -> None:
        self.area = self.width * self.length
        self.volume = self.area * self.height


@dataclass
class Platform:
    """A platform is being assembled!
    Please use integer millimeters for dimensions.
    """

    width: int
    length: int
    height: int = 0
    orientation: str = "horizontal"
    planks: List[Plank] = field(default_factory=list)
    vertical_guards: List[Plank] = field(default_factory=list)
    horizontal_guards: List[Plank] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.is_2d = self.height == 0

        if not self.orientation in ("horizontal", "vertical"):
            raise ValueError(
                f"Orientation can only be `horizontal` or `vertical`. `{self.orientation}`"
            )

    def calculate_plank_positions(self):
        # plank_width / 2 , platform_width - plank_width / 2 , # of planks
        matches = []
        widths = set()
        for plank in self.planks:
            if plank.length == self.length:
                matches.append(plank)
                widths.add(plank.width)

        if len(widths) != 1:
            raise NotImplementedError(
                "Sorry we don't support sets of planks with different widths, yet! "
                + f"Got width values: {widths}"
            )

        width = widths.pop()
        return np.linspace(width / 2, self.length - width / 2, num=len(matches)).astype(
            int
        )
