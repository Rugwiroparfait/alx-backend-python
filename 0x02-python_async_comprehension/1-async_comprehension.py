#!/usr/bin/env python3
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator and return them.

    This coroutine uses an asynchronous comprehension to gather 10 random
    numbers from the async_generator and returns them as a list.

    Returns:
        List[float]: A list of 10 random floats generated by async_generator.
    """
    return [number async for number in async_generator()]
