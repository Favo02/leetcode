class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        maxx = max(nums)
        cur = 0
        lenn = 0
        for n in nums:
            if n == maxx:
                cur += 1
            else:
                lenn = max(lenn, cur)
                cur = 0
        lenn = max(lenn, cur)

        return lenn
