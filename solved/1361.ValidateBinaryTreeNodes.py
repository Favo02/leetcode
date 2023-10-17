from typing import List

class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    roots = [True for _ in range(n)]
    for lc, rc in zip(leftChild, rightChild):
      if lc != -1: roots[lc] = False
      if rc != -1: roots[rc] = False
    roots = list(map(lambda t: t[0], filter(lambda t: t[1], map(lambda t: (t[0], t[1]), enumerate(roots)))))

    if not roots: return False

    visited = set()
    visited.add(roots[0])
    
    queue = [roots[0]]
    while queue:
      cur = queue.pop(0)
      lc = leftChild[cur]
      rc = rightChild[cur]
      if lc != -1:
        if lc in visited:
          return False
        else:
          visited.add(lc)
          queue.append(lc)
      if rc != -1:
        if rc in visited:
          return False
        else:
          visited.add(rc)
          queue.append(rc)
    
    return len(visited) == n

s = Solution()
print(s.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1])) # True
print(s.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1])) # False
print(s.validateBinaryTreeNodes(2, [1,0], [-1,-1])) # False
print(s.validateBinaryTreeNodes(4, [3,-1,1,-1], [-1,-1,0,-1])) # True

