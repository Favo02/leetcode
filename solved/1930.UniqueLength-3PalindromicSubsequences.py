class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:

    pal = 0
    alf = "qwertyuiopasdfghjklzxcvbnm"

    for let in alf:
      if let not in s: continue

      first = s.index(let)
      last = s.rindex(let)

      if first == last: continue

      pal += len(set(s[first+1:last]))

    print(pal)
    return pal

s = Solution()
s.countPalindromicSubsequence("aabca") # 3 aba aaa aca
s.countPalindromicSubsequence("adc") # 0
s.countPalindromicSubsequence("bbcbaba") # 4
