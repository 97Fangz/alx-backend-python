#!/usr/bin/env python3
""" Measure the runtime """

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ measures the total execution time for wait_n(n, max_delay)
    Parameters
    ----------
    n : int
        number of execution
    max_delay : int
        maximum delay

    Returns
    -------
    float
        runtime per execution (total_time /n)
    """
    elapsed_time: float

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
