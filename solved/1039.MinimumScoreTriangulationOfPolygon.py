from typing import List
from functools import cache

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @cache
        def solve(l, r):
            if r - l < 3:
                return 0

            if r - l == 3:
                return values[l] * values[l+1] * values[l+2]

            res = float("inf")
            for c in range(l+1, r-1):
                res = min(res, (values[r-1] * values[l] * values[c]) + solve(l, c+1) + solve(c, r))
            return res

        return solve(0, len(values))
