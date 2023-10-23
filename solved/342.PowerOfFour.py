import math

class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    return n > 0 and math.log(n, 4) % 1 == 0

s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(5))
print(s.isPowerOfFour(1))
