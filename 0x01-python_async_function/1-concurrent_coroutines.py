#!/usr/bin/env python3
"""Module 1-concurrent_coroutines.

This module provides a function to execute multiple coroutines
concurrently and return the results in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with a specified max_delay
    and returns the list of all delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random coroutine.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
