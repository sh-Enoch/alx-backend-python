#!/usr/bin/env python3
"""
module to returns 10 random numbers using async comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension- function to return 10 random numbers
    Arguments:
        no arguments
    Returns:
        10 random numbers
    """
    rtrn = [p async for p in async_generator()]
    return rtrn
