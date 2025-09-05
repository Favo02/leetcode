class Solution:
    def makeTheIntegerZero(self, N: int, M: int) -> int:
        for i in range(61):
            n = N - M*i
            if n >= 0 and n.bit_count() <= i <= n:
                return i
        return -1
