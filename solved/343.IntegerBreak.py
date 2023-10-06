class Solution:
  def integerBreak(self, n: int) -> int:

    if n == 2:
      print(1)
      return 1
    if n == 3:
      print(2)
      return 2

    res = 0
    for k in range(2, (n//2)+1):
      floor = n // k
      mul = 0

      if floor * k == n:
        mul = floor**k
      else:
        numRoof = n - (floor * k)
        mul = ((floor+1)**numRoof) * (floor**(k - numRoof))
      res = max(res, mul)

    print(res)
    return res

s = Solution()
s.integerBreak(2)
s.integerBreak(3)
s.integerBreak(4)
s.integerBreak(10)
