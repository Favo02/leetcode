class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxx = reduce(lambda a, b: a | b, nums)

        def solve(i, cur):
            if i == len(nums):
                return cur == maxx and 1 or 0

            return solve(i+1, cur) + solve(i+1, cur | nums[i])

        return solve(0, 0)
