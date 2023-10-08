#!/usr/bin/env python3

'''
duck-typed annotations
'''

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:

    '''
   First element of a sequence if it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
