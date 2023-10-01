class Solution:
  def reverseWords(self, s: str) -> str:
    res = []
    for w in s.split(" "):
      res.append("".join(reversed(w)))
    return " ".join(res)

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords("God Ding"))
