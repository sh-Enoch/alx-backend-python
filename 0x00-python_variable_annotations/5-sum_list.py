#!/usr/bin/env python3
"""Type-annotate function sum_list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Take input_list and return's their sum."""
    return sum(input_list)
