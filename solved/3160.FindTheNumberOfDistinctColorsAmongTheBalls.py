from typing import List
from collections import defaultdict

class Solution:
  def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    res = []

    balls = {}
    colors = defaultdict(set)

    for ball, color in queries:
      if ball in balls:
        colors[balls[ball]].remove(ball)
        if len(colors[balls[ball]]) == 0:
          del colors[balls[ball]]

      balls[ball] = color
      colors[color].add(ball)

      res.append(len(colors))

    print(res)
    return res

s = Solution()
s.queryResults(4, queries = [[1,4],[2,5],[1,3],[3,4]])
s.queryResults(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]])
