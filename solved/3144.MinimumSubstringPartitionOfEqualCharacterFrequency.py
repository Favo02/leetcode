import sys
sys.setrecursionlimit(10**8)

class Solution:
  def minimumSubstringsInPartition(self, s: str) -> int:

    def ti(letter):
      return ord(letter) - ord('a')

    def valid(count):
      num = 0
      for c in count:
        if c == 0:
          continue
        if num == 0:
          num = c
        else:
          if num != c:
            return False
      return True

    def solve(i, count):
      t = tuple(count)
      if (i, t) in mem:
        return mem[(i, t)]

      if i == len(s):
        return 0

      res = float('inf')

      for j, c in enumerate(s[i:]):
        count[ti(c)] += 1
        if valid(count):
          res = min(res, 1 + solve(i+j+1, [0] * 26))

      mem[(i, t)] = res
      return res

    mem = {}
    return solve(0, [0] * 26)

s = Solution()
print(s.minimumSubstringsInPartition("fabccddg"))
print(s.minimumSubstringsInPartition("abababaccddb"))
print(s.minimumSubstringsInPartition("xwjhpcyyyyrpppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhxwjhpcyyyyrpppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjh"))
print(s.minimumSubstringsInPartition("xwjhpcyyyyrpppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsrrrssxxxfnnnhhjqnrsrntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrpppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsrrrssxxxfnnnhhjqnrsrntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrpppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsrrrssxxxfnnnhhjqnrsrntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrpppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsrrrssxxxfnnnhhjqnrsrntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrpppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsrrrssxxxfnnnhhjqnrsrntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnntttxwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnnttt"))
