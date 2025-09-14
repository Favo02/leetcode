from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(24):
            cur = 0
            for c in candidates:
                if ((1 << i) & c) != 0:
                    cur += 1
            res = max(res, cur)
        return res
