#!/usr/bin/env python3
""" Tasks """

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ returns asyncio.Task object after waiting for random delay
    Parameters
    ----------
    max_delay : int
        maximum delay in seconds

    Returns
    -------
        asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
