class Solution:
  def generateKey(self, num1: int, num2: int, num3: int) -> int:
    a = "0000" + str(num1)
    b = "0000" + str(num2)
    c = "0000" + str(num3)

    res = ""
    for i in range(4):
      res += min(a[-i-1], b[-i-1], c[-i-1])
    print(int(res[::-1]))
    return int(res[::-1])

s = Solution()
s.generateKey(num1 = 1, num2 = 10, num3 = 1000)
s.generateKey(987, num2 = 879, num3 = 798)
s.generateKey(1, num2 = 2, num3 = 3)

