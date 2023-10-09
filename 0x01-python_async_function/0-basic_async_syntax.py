#!/usr/bin/env python3
"""write asynchronous coroutine that takes in an integer argument
waits for a random delay between 0 and max_delay
seconds and eventually returns it """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for a random delay and return the delay
    Parmeters
    ---------
    max_delay : int
        maximum delay

    Returns
    -------
    int
        random delay between 0 and max_delay (included and float value)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
