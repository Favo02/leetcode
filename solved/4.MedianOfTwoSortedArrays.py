from typing import List

def median(arr):
  L = len(arr)
  if L == 0:
    return -1
  if L % 2 == 0:
    return (arr[L // 2 -1] + arr[L // 2]) / 2
  else:
    return arr[L // 2]

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()
    return median(nums)

s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,7]))
