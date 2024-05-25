from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

    wordDict = set(wordDict)

    def solve(i):
      res = []

      for j in range(i, len(s)):
        if s[i:j+1] in wordDict:

          if j+1 == len(s):
            res.append(s[i:j+1])

          valid, words = solve(j+1)
          if valid:
            res += [s[i:j+1] + ' ' + w for w in words]

      if len(res) == 0:
        return False, []
      return True, res


    _, res = solve(0)
    print(res)
    return res

s = Solution()
s.wordBreak("catsanddog", wordDict = ["cat","cats","and","sand","dog"])
s.wordBreak("pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"])
