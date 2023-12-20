class Solution:
  def buyChoco(self, prices: List[int], money: int) -> int:
    a,b = prices[0], prices[1]
    a,b = min(a,b), max(a,b)

    for n in prices[2:]:
      if n < a:
        b = a
        a = n
      elif n < b:
        b = n

    return (money - a - b) if (a+b <= money) else money
