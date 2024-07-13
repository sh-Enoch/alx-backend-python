#!/usr/bin/env python3
"""Measure runtime."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Execute async_comprehension 4 times and measure time."""
    start = time.perf_counter()
    t = async_comprehension()
    await asyncio.gather(t, t, t, t)
    end = time.perf_counter() - start
    return end
