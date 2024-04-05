class Solution:
  def makeGood(self, s: str) -> str:
    diff = ord('a') - ord('A')
    res = []
    for c in s:
      if len(res) > 0 and abs(ord(res[-1]) - ord(c)) == diff:
        res = res[:-1]
      else:
        res.append(c)
    return "".join(res)
