#!/usr/bin/env python3
'''Six.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Calculates the sum of a list of integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))
