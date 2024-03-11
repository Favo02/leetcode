class Solution:
  def customSortString(self, order: str, s: str) -> str:
    return "".join(sorted(list(s), key=lambda a: order.index(a) if a in order else -1))
