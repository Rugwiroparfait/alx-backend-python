#!/usr/bin/env python3
import asyncio
import random
from typing import Generator
"""
    Asynchronously generates random numbers.

    This coroutine will loop 10 times, each time
    asynchronously waiting for 1 second,
    and then yielding a random float between 0 and 10.

    Returns:
        Generator[float, None, None]: A generator that yields random floats.
    """


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random numbers.

    This coroutine will loop 10 times, each time
    asynchronously waiting for 1 second,
    and then yielding a random float between 0 and 10.

    Returns:
        Generator[float, None, None]: A generator that yields random floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
