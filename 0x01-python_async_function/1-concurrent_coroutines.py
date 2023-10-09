#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ execute wait_random from 0-basic_async_syntax.py file
    n times with the specified max_delay

    Parameters
    ----------
    n : int
      number of times to execute wait_random
    max_delay : int
        maximum delay

    Returns
    -------
    list
        list of all the delays (float values) returned from wait_random
    """
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
