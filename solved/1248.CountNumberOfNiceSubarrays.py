class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        res = 0
        start = odd = even_before = 0
        for n in nums:
            if n % 2 == 1:
                even_before = 0
                odd += 1

            while odd > k:
                if nums[start] % 2 == 1:
                    odd -= 1
                start += 1

            if odd == k:
                while nums[start] % 2 == 0:
                    even_before += 1
                    start += 1
                res += even_before+1

        return res
