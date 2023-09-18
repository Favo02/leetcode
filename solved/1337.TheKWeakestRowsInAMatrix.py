from typing import List

class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    for i, m in enumerate(mat):
      mat[i] = (sum(m), i)
    mat.sort()

    res = []
    for i in range(k):
      res.append(mat[i][1])

    print(res)
    return res

s = Solution()
s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 2)
