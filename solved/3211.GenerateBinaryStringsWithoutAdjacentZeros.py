from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:

        def solve(rem, last):
            if rem == 1:
                if last == 0:
                    return ['1']
                return ['0', '1']

            if last == 0:
                return ['1' + r for r in solve(rem-1, 1)]
            return ['1' + r for r in solve(rem-1, 1)] + ['0' + r for r in solve(rem-1, 0)]

        return solve(n, -1)

s = Solution()
s.validStrings(3)
