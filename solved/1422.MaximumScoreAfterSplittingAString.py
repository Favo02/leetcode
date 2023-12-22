class Solution:
  def maxScore(self, s: str) -> int:
    num = [int(n) for n in s]
    score = 0
    for i in range(1,len(s)):
      newscore = i-sum(num[:i]) + sum(num[i:])
      score = max(score, newscore)
    return score
