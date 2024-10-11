class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
            stack = deque()
            for i, n in enumerate(nums):
                if not stack or n < nums[stack[-1]]:
                    stack.append(i)

            res = 0
            for i, n in enumerate(reversed(nums)):
                lasti = -1
                while stack and nums[stack[-1]] <= n:
                    lasti = stack.pop()

                if lasti != -1:
                    res = max(res, len(nums)-i-1 - lasti)

            return res
