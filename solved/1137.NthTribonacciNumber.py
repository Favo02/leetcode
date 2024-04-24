class Solution:
  def tribonacci(self, n: int) -> int:
    if n == 0:
      return 0

    last = [ 0, 1 ]
    for _ in range(n-1):
      last.append(sum(last))
      last = last[-3:]

    return last[-1]
