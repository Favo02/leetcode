# biweekly contest 114

from typing import List

def isOver(coll):
  for c in coll:
    if c == False:
      return False
  return True

class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    coll = [False for _ in range(k)]
    count = 0
    for n in reversed(nums):
      count += 1
      if n <= k:
        coll[n-1] = True
      if isOver(coll):
        return count

    
      
s = Solution()
print(s.minOperations(nums = [3,1,5,4,2], k = 2))
print(s.minOperations(nums = [3,1,5,4,2], k = 5))
print(s.minOperations(nums = [3,2,5,3,1], k = 3))
      
