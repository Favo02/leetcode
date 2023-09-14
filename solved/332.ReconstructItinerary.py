def buildGraph(tickets):
  graph = {}
  for t in tickets:
    fr = t[0]
    to = t[1]
    if fr in graph:
      graph[fr].append(to)
    else:
      graph[fr] = [ to ]
    if to not in graph:
      graph[to] = []
  for k in graph:
    graph[k].sort()
  return graph

def solve(nTickets, graph, cur, path):

  if len(path) == nTickets+1:
    return True, path

  for to in graph[cur]:
    # newG = copy.deepcopy(graph)
    graph[cur].remove(to)
    newP = path.copy()
    newP.append(to)
    res = solve(nTickets, graph, to, newP)
    if res[0]:
      return True, res[1]
    # revert graph to old state
    graph[cur].append(to)
    graph[cur].sort()

  return False, []

class Solution(object):
  def findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = buildGraph(tickets)
    path = solve(len(tickets), graph, "JFK", ["JFK"])
    print(path)
    return path[1]


Solution.findItinerary(0, [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
Solution.findItinerary(0, [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
Solution.findItinerary(0, [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])

