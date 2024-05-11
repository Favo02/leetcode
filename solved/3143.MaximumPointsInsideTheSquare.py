from typing import List
from collections import defaultdict

class Solution:
  def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:

    points = [max(abs(x), abs(y)) for x,y in points]

    dist = defaultdict(list)
    for p, l in zip(points, s):
      dist[p].append(l)

    seen = set()
    res = 0

    for p in sorted(dist.keys()):
      labels = dist[p]

      for l in labels:
        if l in seen:
          return res
        seen.add(l)
      res += len(labels)

    return len(points)

s = Solution()
print(s.maxPointsInsideSquare([[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"))
print(s.maxPointsInsideSquare([[1,1],[-2,-2],[-2,2]], s = "abb"))
print(s.maxPointsInsideSquare([[1,1],[-1,-1],[2,-2]], s = "ccd"))
