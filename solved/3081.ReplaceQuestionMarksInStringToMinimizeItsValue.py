from collections import Counter
import string

class Solution:
  def minimizeStringValue(self, s: str) -> str:
    count = Counter(s)
    available = string.ascii_lowercase

    num = s.count("?")

    toinsert = []
    for _ in range(num):
      minn = float("inf")
      mina = None
      for a in available:
        if count[a] < minn:
          mina = a
          minn = count[a]
      assert mina
      toinsert.append(mina)
      count[mina] += 1
    toinsert.sort()

    ti = 0
    res = []
    for ss in s:
      if ss != "?":
        res.append(ss)
      else:
        res.append(toinsert[ti])
        ti += 1

    return "".join(res)

s = Solution()
print(s.minimizeStringValue("???"))
print(s.minimizeStringValue("a?a?"))
print(s.minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
print(s.minimizeStringValue("eq?umjlasi"))
