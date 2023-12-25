def solve(s, mem={}):
  if s in mem:
    return mem[s]

  res = None

  # end of string reached, one possible solution
  if len(s) == 0:
    res = 1
  # string starting with "0", impossible to decode, no solutions
  elif s[0] == "0":
    res = 0
  # string of length 1 (not "0"), one possible solution
  elif len(s) == 1:
    res = 1
  # long string, check wheter next two digits can be a couple
  else:
    a, b = int(s[0]), int(s[1])
    # valid next two digits as a couple,
    # check both cases where next digit is alone and where are a couple
    if (a == 1) or (a == 2 and b <= 6):
      res = solve(s[1:], mem) + solve(s[2:], mem)
    # not possible: solve only for first digit alone
    else:
      res = solve(s[1:], mem)

  mem[s] = res
  return res

class Solution:
  def numDecodings(self, s: str) -> int:
    res = solve(s)
    print(res)
    return res

s = Solution()
s.numDecodings("12") # 2
s.numDecodings("226") # 3
s.numDecodings("06") # 0
s.numDecodings("2101") # 1
