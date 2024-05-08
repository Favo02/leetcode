from collections import defaultdict

class Solution:
  def wonderfulSubstrings(self, word: str) -> int:

    res = 0
    odd = 0 # bitmask
    seen = defaultdict(int)
    seen[odd] = 1

    for c in word:

      odd ^= (1 << ord(c) - ord('a'))
      res += seen[odd]

      for i in range(10):
        res += seen[odd ^ (1 << i)]

      seen[odd] += 1

    print(res)
    return res

s = Solution()
# s.wonderfulSubstrings("aba")
s.wonderfulSubstrings("aabb")
