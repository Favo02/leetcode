class Solution(object):
  def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1]]
    for i in range (numRows-1):
      newL = list(res[i])
      for j in range (1, len(newL)):
        newL[j] = res[i][j-1] + res[i][j]
      newL.append(1)
      res.append(newL)
    return res
      

Solution.generate(0, 30)
