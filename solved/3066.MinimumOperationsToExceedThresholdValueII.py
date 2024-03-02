from typing import List
from collections import Counter
import bisect

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return -1


class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    op = lambda x,y: min(x, y) * 2 + max(x, y)

    res = 0
    count = Counter(nums)

    keys = sorted([c for c in count])

    # bisect.insort(arr, 3)

    while keys:
      # print(count)
      if keys[0] >= k: break
      a = keys[0]

      res += 1

      if count[a] >= 2:
        count[a] -= 2

        newk = op(a,a)
        count[newk] += 1
        if binary_search(keys, newk) == -1:
          bisect.insort(keys, newk)

        if count[a] == 0:
          keys.pop(0)
      else:
        b = keys[1]
        count[a] -= 1
        count[b] -= 1
        assert count[a] == 0
        assert count[b] >= 0

        newk = op(a,b)
        count[newk] += 1
        if binary_search(keys, newk) == -1:
          bisect.insort(keys, newk)

        keys.pop(0)
        if count[b] == 0:
          keys.pop(0)

    print(res)
    return res

s = Solution()
s.minOperations(nums = [2,11,10,1,3], k = 10) # 2
s.minOperations(nums = [1,1,2,4,9], k = 20) # 4
s.minOperations([999,999,999], 1000)
