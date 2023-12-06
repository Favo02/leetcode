class Solution:
  def totalMoney(self, n: int) -> int:
    res = 0

    lastDay = 0
    lastMonday = 0
    toNextMonday = 1

    while n > 0:
      if toNextMonday == 1:
        lastDay = lastMonday
        lastMonday += 1
        toNextMonday = 7
      else:
        toNextMonday -= 1

      res += lastDay+1
      lastDay = lastDay+1
      n -= 1

    print(res)
    return res

s = Solution()
s.totalMoney(4)
s.totalMoney(10)
s.totalMoney(20)
