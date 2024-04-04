class Solution:
  def maxDepth(self, s: str) -> int:
    res = cur = 0
    for p in s:
      if p == "(":
        cur += 1
      if p == ")":
        cur -= 1
      assert cur >= 0
      res = max(res, cur)
    return res
