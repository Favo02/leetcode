from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(n):
            if '0' in str(a) or '0' in str(n-a):
                continue
            return [a, n-a]
