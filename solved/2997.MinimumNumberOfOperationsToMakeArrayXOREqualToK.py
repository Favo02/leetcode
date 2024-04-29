from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        length = max(len(bin(k)), len(bin(max(nums))))
        res = 0
        for i in range(length):
            target = (k & (1 << i))
            ones = 0 
            for n in nums:
                if (n & (1 << i)) != 0:
                    ones += 1
            if target == 0:
                if ones % 2 != 0:
                    res += 1
            else:
                if ones % 2 != 1:
                    res += 1
        print(res)
        return res

s = Solution()
s.minOperations([2,1,3,4], 1)
s.minOperations([2,0,2,0], 0)
