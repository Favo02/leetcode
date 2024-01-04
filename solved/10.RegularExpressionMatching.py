class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    p = re.sub("[*]+", "*", p)
    res = re.fullmatch(p, s)
    return res
