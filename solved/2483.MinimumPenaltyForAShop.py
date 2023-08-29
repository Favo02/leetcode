class Solution(object):
  def bestClosingTime(self, customers):
    """
    :type customers: str
    :rtype: int
    """

    N = len(customers)

    clients = []
    empty = []

    ccount = 0
    ecount = 0

    j = N-1
    for i in range(N):

      empty.append(ecount)
      ccount += 1 if customers[j] == 'Y' else 0
      ecount += 1 if customers[i] == 'N' else 0
      clients.append(ccount)

      j -= 1

    clients.reverse()

    min = empty[0] + clients[0]
    minI = 0
    for i in range(N):
      pen = empty[i] + clients[i]
      if pen < min:
        min = pen
        minI = i

    # edge case best time greather than array length
    if calculate(customers, N) < min:
      minI = N
    
    print(minI)
    return minI


def calculate(customers, closing):
  penalty = 0

  for i in range(len(customers)):
    if (i < closing):
      penalty += 1 if customers[i] == 'N' else 0
    else:
      penalty += 1 if customers[i] == 'Y' else 0

  return penalty

Solution.bestClosingTime(None, "YNYY"); # 4
Solution.bestClosingTime(None, "YYNY"); # 2
Solution.bestClosingTime(None, "NYYYYNYN"); # 5
Solution.bestClosingTime(None, "YYYY"); # 4
Solution.bestClosingTime(None, "NNNNN"); # 0
