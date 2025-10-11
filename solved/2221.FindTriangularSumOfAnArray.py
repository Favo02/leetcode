from typing import List
from math import comb
from functools import reduce

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        return reduce(lambda acc, el: (acc + comb(len(nums)-1, el[0]) * el[1]) % 10, enumerate(nums), 0)
