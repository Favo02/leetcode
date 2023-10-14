from typing import List

class Solution:
  def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
    res = []
    lastG = -1
    for i,g in enumerate(groups):
      if g != lastG:
        res.append(words[i])
        lastG = g
    print(res)
    return res

s = Solution()
s.getWordsInLongestSubsequence(n = 3, words = ["e","a","b"], groups = [0,0,1])
s.getWordsInLongestSubsequence(n = 4, words = ["a","b","c","d"], groups = [1,0,1,1])
