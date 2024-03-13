class Solution:
  def pivotInteger(self, n: int) -> int:

    start = (n * (n+1)) / 2
    end = n
    pivot = n

    while start > end:
      end += pivot
      pivot -= 1
      start -= pivot

    if start == end:
      return pivot

    return -1
