class Solution:
  def clearDigits(self, s: str) -> str:

    i = 0
    while i < len(s):
      if s[i].isdigit():
        s = s[:i-1] + s[i+1:]
        i -= 1
      else:
        i += 1

    print(s)

s = Solution()
s.clearDigits("abc")
s.clearDigits("cb34")
s.clearDigits("1cb34")
