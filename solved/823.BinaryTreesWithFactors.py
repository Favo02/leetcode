class Solution:
  def numFactoredBinaryTrees(self, arr: List[int]) -> int:
    MOD = 10**9 + 7

    def pair_factors(n):
      factors_list = []
      for i in arr:
        if i > int(n**0.5):
          break
        if n % i == 0 and n//i in nums:
          factors_list.append((i, n//i))
      return factors_list

    arr.sort()
    fac = {}
    nums = set(arr)

    res = 0

    for n in arr:
      res += 1
      cur = 0

      for a,b in pair_factors(n):
        subtrees = 1 + fac[a] + fac[b] + fac[a] * fac[b]
        if a != b:
          subtrees *= 2
        cur += subtrees

      fac[n] = cur % MOD
      res = (res + cur) % MOD

    return res
