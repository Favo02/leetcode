class Solution:
    def minOperations(self, nums: List[int]) -> int:
        last = nums[0]
        res = 0
        for n in nums[1:]:
            nexxt = max(n, last+1)
            if nexxt != n:
                res += nexxt - n
            last = nexxt
        return res
