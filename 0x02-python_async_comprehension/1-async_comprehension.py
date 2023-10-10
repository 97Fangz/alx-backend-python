#!/usr/bin/env python3

"""
Import async_generator from the previous task
write a coroutine called async_comprehension
that takes no arguments.
coroutine will collect 10 random numbers using an async
comprehensing over async_generator
return the 10 random numbers.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect random numbers using async
    """
    return [i async for i in async_generator()]
