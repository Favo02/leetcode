class Solution:
  def numberOfWays(self, corridor: str) -> int:
    MOD = 10**9 + 7
    res = 1

    seats = 0
    buffer = 0

    for i in corridor:
      if i == 'S':
        seats += 1

      if seats > 0 and seats % 2 == 0:
        buffer += 1

      if seats == 3:
        res = (res * buffer) % MOD
        seats = 1
        buffer = 0

    if seats != 2:
      res = 0

    print(res % MOD)
    return res % MOD

s = Solution()
s.numberOfWays("SSPPSPS") # 3
s.numberOfWays("SPSSSSPS") # 1
s.numberOfWays("PPSPSP") # 1
s.numberOfWays("S") # 0
s.numberOfWays("SPSPPSSPSSSS") # 6
s.numberOfWays("PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS") # 919999993
