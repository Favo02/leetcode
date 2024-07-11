class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        lenn = [1] * len(nums)
        times = [1] * len(nums)

        maxx = 0
        res = 0

        for inum in range(len(nums)):

            for ilen in range(inum):

                if nums[inum] > nums[ilen]:

                    if lenn[ilen]+1 > lenn[inum]:
                        lenn[inum] = lenn[ilen]+1
                        times[inum] = times[ilen]
                    elif lenn[ilen]+1 == lenn[inum]:
                        times[inum] += times[ilen]

            if lenn[inum] > maxx:
                maxx = lenn[inum]
                res = times[inum]
            elif lenn[inum] == maxx:
                res += times[inum]

        return res
