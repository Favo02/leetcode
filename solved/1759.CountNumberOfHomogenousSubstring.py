class Solution:
  def countHomogenous(self, s: str) -> int:
    MOD = (10**9) + 7
    res = 0

    cur = ''
    count = 0

    for l in s:
      if l == cur:
        count += 1
      else:
        sum = ((count * (count+1)) // 2) % MOD
        res = (res + sum) % MOD
        cur = l
        count = 1
    else:
      sum = ((count * (count+1)) // 2) % MOD
      res = (res + sum) % MOD

    print(res)
    return res

s = Solution()
s.countHomogenous("abbcccaa") # 13
s.countHomogenous("xy") # 2
