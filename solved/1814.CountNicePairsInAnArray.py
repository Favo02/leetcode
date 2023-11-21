from typing import List

class Solution:
  def countNicePairs(self, nums: List[int]) -> int:
    MOD = 10**9+7

    res = 0
    found = {}
    for n in nums:
      n = n - int(str(n)[::-1])
      if n in found:
        res = (res + (1*found[n]) % MOD) % MOD
        found[n]+=1
      else:
        found[n]= 1
    print(res)
    return res

s = Solution()
s.countNicePairs([42,11,1,97]) # 2
s.countNicePairs([13,10,35,24,76]) # 4
