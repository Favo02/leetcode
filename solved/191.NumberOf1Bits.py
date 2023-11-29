class Solution:
  def hammingWeight(self, n: int) -> int:
    res = 0
    for i in bin(n)[2:]:
      if i == '1':
        res += 1
    print(res)
    return res

s = Solution()
s.hammingWeight(0b00000000000000000000000000001011)
s.hammingWeight(0b00000000000000000000000010000000)
s.hammingWeight(0b11111111111111111111111111111101)
