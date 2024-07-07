from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        last = None
        start = 0
        res = 0

        for i in range(0, len(colors)+(k-1)):
            if last == colors[i%len(colors)]:
                start = i

            # print(i, start)

            if start is not None and i - start >= (k-1):
                # print(start, i)
                res += 1

            last = colors[i%len(colors)]

        print(res)
        return res

s = Solution()
s.numberOfAlternatingGroups([0,1,0,1,0], k = 3)
s.numberOfAlternatingGroups([0,1,0,0,1,0,1], k = 6)
s.numberOfAlternatingGroups(colors = [1,1,0,1], k = 4)
