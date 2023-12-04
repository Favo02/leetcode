class Solution:
  def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    res = 0
    last = points[0]
    for p in points[1:]:
      res += max(abs(p[0]-last[0]), abs(p[1]-last[1]))
      last = p
    print(res)
    return res
