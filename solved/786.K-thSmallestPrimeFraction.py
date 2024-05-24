from typing import List

class Solution:
  def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

    fracts = []
    for i, a in enumerate(arr):
      for b in arr[i+1:]:
        fracts.append((a/b, a, b))

    fracts.sort()

    return fracts[k-1][1:]

s = Solution()

s.kthSmallestPrimeFraction(arr = [1, 2, 3, 5], k = 3)
# s.kthSmallestPrimeFraction(arr = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59], k = 3)
