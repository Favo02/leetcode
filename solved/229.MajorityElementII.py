from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:  
    target = len(nums) // 3
    dict = {}
    res = set()
    for n in nums:
      if n in dict:
        dict[n] += 1
      else:
        dict[n] = 1
      if dict[n] > target:
        res.add(n)
    
    print(res)
    return res

s = Solution()
s.majorityElement([3,2,3])
s.majorityElement([1])
s.majorityElement([1,2])
