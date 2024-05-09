from typing import List

class Solution:
  def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    happiness.sort(reverse=True)
    return sum([max(0, h - i) for i, h in enumerate(happiness[:k])])
