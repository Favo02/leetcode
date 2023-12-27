from typing import List

class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    res = 0

    last = None
    summ, maxx = 0, 0

    for color, time in zip(colors, neededTime):
      if color == last:
        summ += time
        maxx = max(maxx, time)
      else:
        res += summ-maxx
        summ = maxx = time
      last = color

    res += summ-maxx

    print(res)
    return res

s = Solution()
s.minCost("abaac", [1,2,3,4,5])
s.minCost("abc", [1,2,3])
s.minCost("aabaa", [1,2,3,4,1])
