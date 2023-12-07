from typing import List

def calc_intervals(cols):
  intervals = []
  for c in cols:
    start = -1
    cur_inter = []
    for i, elem in enumerate(c):
      if elem and start == -1:
        start = i
      elif not elem and start != -1:
        cur_inter.append((start, i))
        start = -1
    if start != -1:
      cur_inter.append((start, i+1))
    intervals.append(cur_inter)
  return intervals

def smaller_than(inter1, inter2):
  s1, e1 = inter1
  s2, e2 = inter2
  return s1 >= s2 and e1 <= e2

def has_bigger(inter, col_inters):
  for c in col_inters:
    if smaller_than(inter, c):
      return True
  return False

class Solution:
  def maximalRectangle(self, rows: List[List[str]]) -> int:

    columns = [[int(m[i]) for m in rows] for i in range(len(rows[0]))]
    intervals = calc_intervals(columns)

    maxx = 0

    for i, col_inters in enumerate(intervals):
      for start, e in col_inters:
        # the ends could be not aligned, so the range could not expand horizontally
        # so we need to check every possible height (to align with adjacent intervals)
        for end in range(e, start, -1):

          bound_l = bound_r = i
          while bound_l >= 1 and has_bigger((start, end), intervals[bound_l-1]):
            bound_l -= 1
          while bound_r <= len(intervals)-2 and has_bigger((start, end), intervals[bound_r+1]):
            bound_r += 1

          maxx = max(maxx, (end-start) * (bound_r+1-bound_l))

    print(maxx)
    return maxx

s = Solution()
s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) # 6
s.maximalRectangle([["0"]]) # 0
s.maximalRectangle([["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]) # 6
s.maximalRectangle([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]) # 8
