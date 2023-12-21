class Solution:
  def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    points = [x for x,y in points]
    points.sort()
    maxx = 0
    for p1, p2 in zip(points, points[1:]):
      maxx = max(maxx,(p2 - p1))
    print(maxx)
    return maxx
