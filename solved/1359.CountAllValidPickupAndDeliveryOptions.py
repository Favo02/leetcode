mem = {}

def recursion(toP, toD):
  if toP + toD == 0:
    return 1

  if (toP, toD) in mem:
    return mem[(toP, toD)]
  
  res = 0

  if toP > 0:
    res += toP * recursion(toP-1, toD+1)
  if toD > 0:
    res += toD * recursion(toP, toD-1)

  res %= 1000000007
  mem[(toP, toD)] = res
  return res

class Solution(object):
  def countOrders(self, n):
    """
    :type n: int
    :rtype: int
    """

    res = recursion(n, 0)
    print(res)
    return res

Solution.countOrders(0, 1)
Solution.countOrders(0, 2)
Solution.countOrders(0, 3)
Solution.countOrders(0, 4)
Solution.countOrders(0, 6)
Solution.countOrders(0, 8)
Solution.countOrders(0, 18)
Solution.countOrders(0, 488)
Solution.countOrders(0, 492)
Solution.countOrders(0, 500)
