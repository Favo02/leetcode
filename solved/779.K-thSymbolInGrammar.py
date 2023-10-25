class Solution:
  def kthGrammar(self, n, k):
    inverse = False
    while n > 0:
      lenRow = 2**n
      if k > (lenRow // 2):
        k -= (lenRow // 2)
        inverse = not inverse
      n -= 1
    return 1 if inverse else 0

s = Solution()
print(s.kthGrammar(1,1))
print(s.kthGrammar(2,1))
print(s.kthGrammar(2,2))
print(s.kthGrammar(8,10))
print(s.kthGrammar(30,10))
