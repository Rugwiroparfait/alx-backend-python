#!/usr/bin/env python3
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of four parallel async_comprehensions.

    This coroutine measures the time it takes to run four instances of
    async_comprehension in parallel using asyncio.gather. It returns the
    total runtime as a float.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
