class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) == 0: return True

    target = 0
    for i in t:
      if i == s[target]:
        target += 1
      if target == len(s):
        return True
    return False

s = Solution()
print(s.isSubsequence(s = "abc", t = "ahbgdc"))
print(s.isSubsequence(s = "axc", t = "ahbgdc"))
