from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [i for i in range(1, n)]
        res.append((n-1) * n // 2 * -1)
        return res
