from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def cmp(a, b):
            if a+b < b+a:
                return -1
            if b+a < a+b:
                return 1
            return 0

        nums = sorted(map(str, nums), reverse=True, key=cmp_to_key(cmp))
        return "".join(nums).lstrip("0") or "0"
