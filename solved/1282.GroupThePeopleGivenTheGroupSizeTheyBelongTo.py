def split(list, length):
  res = []
  for i in range(0, len(list), length):
    res.append(list[i:i+length])
  return res

class Solution(object):
  def groupThePeople(self, groupSizes):
    """
    :type groupSizes: List[int]
    :rtype: List[List[int]]
    """
    
    people = {}

    for i, g in enumerate(groupSizes):
      if g in people:
        people[g].append(i)
      else:
        people[g] = [ i ]

    res = []
    for k in people:
      res += split(people[k], k)

    print(res)
    return res

Solution.groupThePeople(0, [3,3,3,3,3,1,3])
