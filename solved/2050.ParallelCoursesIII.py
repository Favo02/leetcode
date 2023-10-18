from typing import List

def buildGraph(n, relations):
  graph = [[] for _ in range(n)]
  for prev, next in relations:
    graph[next].append(prev)
  return graph

def calcTime(target, graph, time):
  if mem[target] != -1:
    return mem[target]

  curmax = time[target]
  for prev in graph[target]:
    curmax = max(curmax, time[target] + calcTime(prev, graph, time))

  mem[target] = curmax
  return curmax

class Solution:
  def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

    global mem
    mem = [-1 for _ in range(n)]

    relations = list(map(lambda r: (r[0]-1, r[1]-1), relations))
    graph = buildGraph(n, relations)

    res = 0
    for course in range(n):
      res = max(res, calcTime(course, graph, time))

    print(res)
    return res

s = Solution()
s.minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5])
s.minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])
