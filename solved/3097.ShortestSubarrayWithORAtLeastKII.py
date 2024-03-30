from typing import List
from collections import defaultdict

class Solution:
  def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    res = float("inf")

    value = 0
    # keep track of on bits (and how many times they have been set)
    # we need that to slide the window, bitwise or does not have an inverse operation
    on_bits = defaultdict(int)

    to_bin = lambda num: reversed(bin(num)[2:])
    remove_bit = lambda num, i: num & ~(1 << i)

    start = 0
    for end in range(0, len(nums)):

      value |= nums[end]
      # update number of on bits
      for i, b in enumerate(to_bin(nums[end])):
        if b == "1":
          on_bits[i] += 1

      # reduce window
      while start <= end and value >= k:
        res = min(res, end-start+1)

        # update on bits counter
        for i, b in enumerate(to_bin(nums[start])):
          if b == "1":
            on_bits[i] -= 1
            # decrease value only if the value removed from window was the only
            # one to set the bit on
            if on_bits[i] == 0:
              value = remove_bit(value, i)

        start += 1

    if res == float("inf"):
      print(-1)
      return -1

    print(res)
    return res

s = Solution()
s.minimumSubarrayLength([1,2,3], k = 2)
s.minimumSubarrayLength([2,1,8], k = 10)
s.minimumSubarrayLength([1,2], k = 0)
