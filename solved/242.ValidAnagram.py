class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    s = sorted(list(s))
    t = sorted(list(t))
    for a,b in zip(s,t):
      if a != b:
        return False
    return True
