from collections import defaultdict

class Solution:
  def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    last = defaultdict(int)
    res = -1

    for i, c in enumerate(s):
      if c in last:
        res = max(res, i-last[c]-1)
      else:
        last[c] = i

    print(res)
    return res

s = Solution()
s.maxLengthBetweenEqualCharacters("aa")
s.maxLengthBetweenEqualCharacters("abca")
s.maxLengthBetweenEqualCharacters("cbzxy")
