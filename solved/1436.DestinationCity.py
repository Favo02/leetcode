class Solution:
  def destCity(self, paths: List[List[str]]) -> str:
    occs = defaultdict(int)
    ignore = set()
    for a,b in paths:
      ignore.add(a)
      occs[a] += 1
      occs[b] += 1
    for city, occ in occs.items():
      if occ == 1 and city not in ignore:
        return city
