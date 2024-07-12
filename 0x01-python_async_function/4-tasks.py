#!/usr/bin/env python3
"""Multi coroutines."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of all delays."""
    ls = [task_wait_random(max_delay) for i in range(n)]
    new_ = []
    for task in asyncio.as_completed(ls):
        t = await task
        new_.append(t)
    return sorted(new_)
