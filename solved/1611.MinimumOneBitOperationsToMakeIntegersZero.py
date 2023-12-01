class Solution:
  def minimumOneBitOperations(self, n: int) -> int:
    n = [int(c) for c in list(bin(n)[2:])]

    res = 0
    flipOp = True
    for i,s in enumerate(n):
      val = 0
      if s == 1:
        val = 2**(len(n)-i)-1
        flipOp = not flipOp

      if flipOp: res += val
      else: res -= val

    print(abs(res))
    return abs(res)

s = Solution()
s.minimumOneBitOperations(3) # 2
s.minimumOneBitOperations(5) # 6
s.minimumOneBitOperations(6) # 4
s.minimumOneBitOperations(9) # 14
s.minimumOneBitOperations(12) # 8
s.minimumOneBitOperations(15) # 10
