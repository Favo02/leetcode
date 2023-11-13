class Solution:
  def sortVowels(self, s: str) -> str:
    vow = "AEIOUaeiou"
    v = list(filter(lambda c: c in vow, s))
    v.sort()

    sortI = 0
    s = list(s)

    for i in range(len(s)):
      if s[i] in vow:
        s[i] = v[sortI]
        sortI += 1

    s = "".join(s)
    print(s)
    return s

s = Solution()
s.sortVowels("lEetcOde")
s.sortVowels("lYmpH")
