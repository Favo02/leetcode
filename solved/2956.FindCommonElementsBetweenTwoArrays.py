from typing import List

class Solution:
  def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
    r1 = r2 = 0
    for n in nums1:
      if n in nums2:
        r1 += 1
    for n in nums2:
      if n in nums1:
        r2 += 1
    print(r1, r2)
    return [r1, r2]

s = Solution()
s.findIntersectionValues(nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6])
s.findIntersectionValues(nums1 = [3,4,2,3], nums2 = [1,5])
