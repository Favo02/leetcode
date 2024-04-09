class Solution:
  def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    kk = tickets[k]
    return sum([min(t, kk) if i <= k else min(t, kk-1) for i, t in enumerate(tickets)])
