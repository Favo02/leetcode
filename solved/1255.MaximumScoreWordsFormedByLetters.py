from collections import Counter
from typing import List

class Solution:
  def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

    def word_score(wordindex, available):
      ws = 0
      for char, count in counts[wordindex].items():
        if count <= available[char]:
          ws += score[ord(char) - ord('a')] * count
        else:
          return 0
      return ws

    def solve(wi, available):
      if wi == len(words):
        return 0

      score = word_score(wi, available)
      if score == 0:
        return solve(wi+1, available)

      newa = available.copy()
      for c in words[wi]:
        newa[c] -= 1

      return max(solve(wi+1, available), score + solve(wi+1, newa))

    counts = [Counter(w) for w in words]
    available = Counter(letters)

    res = solve(0, available)
    print(res)
    return res


s = Solution()
s.maxScoreWords(["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
s.maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
)
s.maxScoreWords(["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])
