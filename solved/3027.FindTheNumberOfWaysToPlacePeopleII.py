from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        L = len(points)
        res = 0

        points.sort(key=lambda p: (p[0], -p[1]))

        for i in range(L):
            xi, yi = points[i]
            limity = float("-inf")
            for j in range(i+1, L):
                xj, yj = points[j]
                assert xi <= xj
                if yi >= yj and limity < yj:
                    res += 1
                    limity = yj

        return res
