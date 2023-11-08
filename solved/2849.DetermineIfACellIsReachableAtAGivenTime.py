class Solution:
  def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    if sx == fx and sy == fy:
      return t != 1
    dx = abs(sx-fx)
    dy = abs(sy-fy)
    return max(dx, dy) <= t

s = Solution()
print(s.isReachableAtTime(sx = 2, sy = 4, fx = 7, fy = 7, t = 6)) # true
print(s.isReachableAtTime(sx = 3, sy = 1, fx = 7, fy = 3, t = 3)) # false
