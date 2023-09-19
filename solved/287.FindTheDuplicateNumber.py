from typing import List

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    found = set()
    for n in nums:
      if n in found:
        return n
      found.add(n)  
