from typing import List
from heapq import heappop, heappush

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        L = len(classes)

        val = sum(p / t for p, t in classes)
        avg = val / L

        improvements = []
        for i in range(L):
            val -= classes[i][0]/classes[i][1]
            val += (classes[i][0]+1)/(classes[i][1]+1)

            delta = (val / L) - avg
            heappush(improvements, (-delta, i))

            val -= (classes[i][0]+1)/(classes[i][1]+1)
            val += classes[i][0]/classes[i][1]

        for _ in range(extraStudents):
            _, i = heappop(improvements)

            val -= classes[i][0]/classes[i][1]
            classes[i][0] += 1
            classes[i][1] += 1
            val += classes[i][0]/classes[i][1]

            avg = val / L

            val -= classes[i][0]/classes[i][1]
            val += (classes[i][0]+1)/(classes[i][1]+1)

            delta = (val / L) - avg
            heappush(improvements, (-delta, i))

            val -= (classes[i][0]+1)/(classes[i][1]+1)
            val += classes[i][0]/classes[i][1]

        return val / L

s = Solution()
s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4)

