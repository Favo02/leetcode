class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        res = []
        for n in nums:
            if n == 2:
                res.append(-1)
                continue

            if (n & (n+1)) == 0:
                res.append(n >> 1)
                continue

            for i in range(32):
                if (n >> i) & 1 == 0:
                    n &= ~(1 << i-1)
                    res.append(n)
                    break

        return res
