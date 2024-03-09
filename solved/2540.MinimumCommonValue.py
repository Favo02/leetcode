class Solution:
  def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    i1 = i2 = 0
    while True:
      if i1 == len(nums1) or i2 == len(nums2):
        return -1
      if nums1[i1] > nums2[i2]:
        i2 += 1
      elif nums2[i2] > nums1[i1]:
        i1 += 1
      else:
        assert nums1[i1] == nums2[i2]
        return nums1[i1]
