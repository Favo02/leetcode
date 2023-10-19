class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    stack1 = []
    for c in s:
      if c == '#':
        if len(stack1) > 0:
          stack1.pop()
      else:
        stack1.append(c)

    stack2 = []
    for c in t:
      if c == '#':
        if len(stack2) > 0:
          stack2.pop()
      else:
        stack2.append(c)

    print(stack1 == stack2)
    return stack1 == stack2

s = Solution()
s.backspaceCompare("ab#c", "ad#c")
s.backspaceCompare("ab##", "c#d#")
s.backspaceCompare("a#c", "b")
s.backspaceCompare("y#fo##f", "y#f#o##f")
