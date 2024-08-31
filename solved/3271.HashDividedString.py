class Solution:
  def stringHash(self, s: str, k: int) -> str:


    substrings = len(s) // k
    n = len(s) // substrings

    # print(n)

    res = []

    summ = 0
    count = 0
    for ss in s:
      summ += ord(ss) - ord('a')
      count += 1

      if count == n:
        res.append(chr((summ % 26) + ord('a')))
        summ = 0
        count = 0

    # print(res)
    print("".join(res))
    return "".join(res)





s = Solution()
s.stringHash(s = "abcd", k = 2)
s.stringHash(s = "mxz", k = 3)
