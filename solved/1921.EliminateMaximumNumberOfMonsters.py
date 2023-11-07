import math
from typing import List

def countTimeGreatherThanIndex(l):
  if not l: return 0
  for i, t in enumerate(l):
    if i+1 >= t:
      return i
  return len(l)

class Solution:
  def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
    timeToReach = list(map(lambda t: math.ceil(t[0]/t[1]), zip(dist,speed)))
    timeToReach.sort()
    return countTimeGreatherThanIndex(timeToReach[1:]) + 1

s = Solution()
print(s.eliminateMaximum([1,3,4], [1,1,1])) # 3
print(s.eliminateMaximum([1,1,2,3], [1,1,1,1])) # 1
print(s.eliminateMaximum([3,2,4], [5,3,2])) # 1
print(s.eliminateMaximum([4,2,8], [2,1,4])) # 2
print(s.eliminateMaximum([3,5,7,4,5], [2,3,6,3,2])) # 2
print(s.eliminateMaximum([4,3,4], [1,1,2])) # 3
