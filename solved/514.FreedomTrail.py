from collections import defaultdict
from functools import lru_cache

class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:

    def dist(fr, to):
      i = (fr - to) % len(ring)
      j = (to - fr) % len(ring)
      return min(i, j)

    @lru_cache(maxsize=None)
    def solve(k, cur):
      if k == len(key):
        return 0

      res = float("inf")
      for pos in positions[key[k]]:
        res = min(res, 1 + dist(cur, pos) + solve(k+1, pos))
      return res

    positions = defaultdict(list)
    for i, k in enumerate(ring):
      if k in key:
        positions[k].append(i)

    res = solve(0, 0)
    print(res)
    return res

s = Solution()
s.findRotateSteps("godding", "gd") # 4
s.findRotateSteps("godding", "godding") # 13
s.findRotateSteps("iotfo", "fioot")
s.findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx")
