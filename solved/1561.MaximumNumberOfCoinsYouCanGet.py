from typing import List

class Solution:
  def maxCoins(self, piles: List[int]) -> int:
    piles.sort()
    res = 0
    minI, maxI = 0, len(piles)-1
    while minI < maxI:
      res += piles[maxI-1]
      maxI -= 2
      minI += 1
    print(res)
    return res
