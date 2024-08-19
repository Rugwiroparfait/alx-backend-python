#!/usr/bin/env python3
"""Module 2-measure_runtime.

This module provides a function to measure
the execution time of concurrent coroutines.
"""

import asyncio
import time
from typing import Any

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n
    and returns the average time per coroutine.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time taken per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
