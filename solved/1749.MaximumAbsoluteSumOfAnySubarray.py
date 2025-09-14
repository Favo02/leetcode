from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curmin = curmax = 0
        res = 0
        for n in nums:
            curmin = min(curmin + n, n)
            curmax = max(curmax + n, n)
            res = max(res, curmax, abs(curmin))
        return res
