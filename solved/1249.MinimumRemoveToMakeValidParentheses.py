class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:

    s = list(s)

    val = 0
    for i, c in enumerate(s):
      if c == '(': val += 1
      if c == ')': val -= 1

      if val < 0:
        s[i] = ''
        val += 1

    i = len(s) -1
    while val > 0:
      if s[i] == '(':
        s[i] = ''
        val -= 1
      i -= 1

    return "".join(s)

s = Solution()
s.minRemoveToMakeValid("lee(t(c)o)de)")
s.minRemoveToMakeValid("a)b(c)d")
s.minRemoveToMakeValid("))((")
