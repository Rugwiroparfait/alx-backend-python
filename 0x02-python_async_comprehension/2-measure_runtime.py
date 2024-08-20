#!/usr/bin/env python3
"""Module 2-measure_runtime.

This module provides a function to measure the total runtime of executing
four parallel instances of an asynchronous comprehension.
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel async_comprehensions.

    This coroutine measures the time it takes to run four instances of
    async_comprehension in parallel using asyncio.gather. The function
    returns the total runtime in seconds.

    Returns:
        float: The total runtime in seconds.
    """
    start_time: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time.time()
    total_runtime: float = end_time - start_time
    return total_runtime
