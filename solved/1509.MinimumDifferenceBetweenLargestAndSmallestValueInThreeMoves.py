class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 4:
            return 0

        nums.sort()
        start = 0
        end = len(nums)-4

        minn = nums[end]-nums[start]
        while end < len(nums):
            minn = min(minn, nums[end]-nums[start])
            start += 1
            end += 1

        return minn
