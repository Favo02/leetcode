class Solution:
  def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    ids = dict(nums1)
    for id, val in nums2:
      ids[id] = ids.get(id, 0) + val
    return sorted(list(ids.items()))
