#!/usr/bin/env python3
""" Tasks """

from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ execute task_wait_random from 3-tasks.py file
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
        list of all the delays returned from task_wait_random
    """
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
