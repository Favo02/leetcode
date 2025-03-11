class Solution:
  def countOfSubstrings(self, word: str, k: int) -> int:
    res = 0

    con = 0
    vow = {v: 0 for v in "aeiou"}

    start = 0
    thrown = 0
    for end in range(len(word)):
      if word[end] in vow:
        vow[word[end]] += 1
      else:
        con += 1

      while con > k:
        thrown = 0
        if word[start] in vow:
          vow[word[start]] -= 1
        else:
          con -= 1
        start += 1

      if all(v > 0 for v in vow.values()) and con == k:
        while word[start] in vow and vow[word[start]] > 1:
          thrown += 1
          vow[word[start]] -= 1
          start += 1

        res += 1 + thrown

    return res

s = Solution()
print(s.countOfSubstrings("aeioqq", 1))
print(s.countOfSubstrings("aeiou", 0))
print(s.countOfSubstrings("ieaouqqieaouqq", 1))
print(s.countOfSubstrings("aeioucaeiou", 1))
