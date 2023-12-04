class Solution:
  def largestGoodInteger(self, num: str) -> str:
    l = str(num)
    cur = []
    Max = -1

    for c in l:
      if cur and c == cur[-1]:
        cur.append(c)
      else:
        cur = [c]
      if len(cur) == 3:
        Max = max(Max, int(c))

    if Max == -1: return ""
    return f"{Max}{Max}{Max}"
