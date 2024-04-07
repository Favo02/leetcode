from functools import lru_cache

class Solution:
  @lru_cache(maxsize=None)
  def solve(self, s: str, i: int, val: int) -> bool:

    for j, c in enumerate(s[i:]):
      if c == '(':
        val += 1
      if c == ')':
        val -= 1
      if c == '*':
        close = False
        if val > 0:
          close = self.solve(s, i+j+1, val-1)
        return self.solve(s, i+j+1, val) or self.solve(s, i+j+1, val+1) or close

      if val < 0:
        return False

    return val == 0

  def checkValidString(self, s: str) -> bool:
    return self.solve(s, 0, 0)

s = Solution()
print(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(s.checkValidString("(*()))*("))
