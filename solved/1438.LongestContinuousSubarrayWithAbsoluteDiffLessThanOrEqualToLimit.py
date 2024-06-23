class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        res = start = 0

        minheap = []
        maxheap = []

        for end, n in enumerate(nums):
            heapq.heappush(minheap, (n, end))
            heapq.heappush(maxheap, (-n, end))

            while True:
                minn = None
                while True:
                    minn = minheap[0]
                    if minn[1] >= start:
                        minn = minn[0]
                        break
                    else:
                        heapq.heappop(minheap)

                maxx = None
                while True:
                    maxx = maxheap[0]
                    if maxx[1] >= start:
                        maxx = maxx[0]
                        break
                    else:
                        heapq.heappop(maxheap)
                maxx = -maxx

                if maxx - minn > limit:
                    start += 1
                else:
                    break

            print(minn, maxx)
            res = max(res, end-start+1)

        return res

