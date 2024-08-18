class Solution:
    def nthUglyNumber(self, n: int) -> int:

        mults = [2,3,5]

        nums = [1]
        seen = set(nums)
        heapify(nums)

        while n > 0:
            cur = heappop(nums)
            for m in mults:
                new = cur*m
                if new in seen:
                    continue
                heappush(nums, new)
                seen.add(new)
            n -= 1

        return cur
