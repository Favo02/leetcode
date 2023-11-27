class Solution:
  def knightDialer(self, n: int) -> int:
    MOD = 10**9 + 7

    jumps = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
    last = [1 for _ in range(10)]

    for _ in range(n-1):
      newLast = []
      for curPlace in range(10):
        res = 0
        for j in jumps[curPlace]:
          res = (res + last[j]) % MOD
        newLast.append(res)

      last = newLast

    res = sum(last) % MOD
    print(res)
    return res

s = Solution()
s.knightDialer(1) # 10
s.knightDialer(2) # 20
s.knightDialer(3) # 46
s.knightDialer(4) # 104
s.knightDialer(3131) # 136006598
