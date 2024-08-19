#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """

    Args:
        max_delay (int, optional): Waits for a random delay between 0 and max_delay seconds/
        and returns the delay. Defaults to 10.

    Returns:
        float: maximum delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay