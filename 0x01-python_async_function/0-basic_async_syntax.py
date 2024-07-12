#!/usr/bin/env python3
"""Async coroutine."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async Coro."""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return random.uniform(0, max_delay)
