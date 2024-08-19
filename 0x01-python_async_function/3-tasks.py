#!/usr/bin/env python3
"""Module 3-tasks.

This module provides a function to create
asyncio tasks using the wait_random coroutine.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in
        seconds for the wait_random coroutine.

    Returns:
        asyncio.Task: A Task object that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
