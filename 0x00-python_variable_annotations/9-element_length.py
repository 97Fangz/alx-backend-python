#!/usr/bin/env python3

'''
function’s parameters that return values with the appropriate types
'''

from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    '''
    returns the length of the list of sequences.
    '''

    return [(i, len(i)) for i in lst]
