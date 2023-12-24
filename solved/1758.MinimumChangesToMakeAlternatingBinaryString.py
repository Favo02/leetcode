class Solution:
  def minOperations(self, s: str) -> int:
    res1 = res2 = 0
    for i, c in enumerate(s):
      if c == str(i%2):
        res1 += 1
      if c != str(i%2):
        res2 += 1
    return min(res1, res2)
