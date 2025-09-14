from typing import List
from math import ceil

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            ops = 0
            for exp in range(100):
                low, high = 4**exp, 4**(exp+1) - 1
                if high < l: continue
                if low > r: break
                amount = (high - low + 1) - max(l - low, 0) - max(high - r, 0)
                ops += amount * (exp+1)
            res += ceil(ops / 2)
        print(res)
        return res
