#!/usr/bin/env pyhton3
"""Make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplier by float multiplication."""
    def multiplier_func(number: float) -> float:
        """Multiplies float by multiplier."""
        return multiplier * number

    return multiplier_func
