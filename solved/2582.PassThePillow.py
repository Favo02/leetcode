class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = (n-1)*2
        res = 1 + (time % p)

        if res > n:
            res = n - (res-n)

        return res
