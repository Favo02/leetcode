class Solution:
  def numberOfSubstrings(self, s: str) -> int:

    freqs = {c: 0 for c in "abc"}
    res = 0

    start = 0
    for end in range(0, len(s)):
      freqs[s[end]] += 1

      if all(f > 0 for f in freqs.values()):
        thrown = 0
        while freqs[s[start]] > 1:
          freqs[s[start]] -= 1
          start += 1
          thrown += 1
        after = len(s)-end-1

        res += 1 + thrown + after + thrown * after

        freqs[s[start]] -= 1
        start += 1

    return res

s = Solution()
print(s.numberOfSubstrings("abcabc"))
print(s.numberOfSubstrings("aaacb"))
print(s.numberOfSubstrings("abc"))
