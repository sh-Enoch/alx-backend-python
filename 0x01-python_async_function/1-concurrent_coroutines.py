#!/usr/bin/env python3
"""Multi coroutines."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Retrun list of all delays."""
    ls: List[float] = []
    for obj in range(n):
        new_values = await wait_random(max_delay)
        ls.append(new_values)

    return sorted(ls)
