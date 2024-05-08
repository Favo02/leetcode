from typing import List
from operator import itemgetter

class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    for r, (i, _) in enumerate(sorted(list(enumerate(score)), reverse=True, key=itemgetter(1))):
      score[i] = {0:"Gold Medal", 1:"Silver Medal", 2:"Bronze Medal"}[r] if r < 3 else str(r+1)
    return score

s = Solution()
print(s.findRelativeRanks([4,5,3,2,1]))
