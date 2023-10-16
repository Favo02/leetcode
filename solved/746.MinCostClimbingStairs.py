from typing import List

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    
    for i in range(2, len(cost)):
      cost[i] += min(cost[i-1], cost[i-2])

    return min(cost[-1], cost[-2])

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
