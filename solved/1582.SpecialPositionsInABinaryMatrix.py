class Solution:
  def numSpecial(self, mat: List[List[int]]) -> int:
    res = 0
    for row in mat:
      for x, v in enumerate(row):
        if (v == 1) and (row.count(1) == 1) and ([r[x] for r in mat].count(1) == 1):
          res += 1
    return res
