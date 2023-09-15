def prim(points, start):

  w = 0
  tree = set()
  tree.add(start)

  available = {}
  for p in points:
    if p in tree: continue
    available[p] = manDistance(start, p)

  while len(tree) < len(points):

    min = 1_000_000_000_000
    minP = None
    for k in available:
      if k in tree: continue
      if available[k] < min:
        min = available[k]
        minP = k

    tree.add(minP)
    w += min

    for p in points:
      if p in tree: continue
      md = manDistance(minP, p)
      if md < available[p]:
        available[p] = md

  return tree, w
    
manDistance = lambda p1, p2 : abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

class Solution(object):
  def minCostConnectPoints(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    newPoints = []
    for p in points:
      newPoints.append((p[0], p[1]))
    points = newPoints
    mst, w = prim(points, points[0])
    # print(mst, w)
    print(w)
    return w

Solution.minCostConnectPoints(0, [[0,0],[2,2],[3,10],[5,2],[7,0]])
Solution.minCostConnectPoints(0, [[3,12],[-2,5],[-4,1]])
Solution.minCostConnectPoints(0, [[-1000000,-1000000],[1000000,1000000]])


