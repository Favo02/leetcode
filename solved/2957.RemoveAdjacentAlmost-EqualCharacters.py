class Solution:
  def removeAlmostEqualCharacters(self, word: str) -> int:
    res = 0
    print(word)
    dists = [abs(ord(word[i]) - ord(word[i-1])) for i in range(1, len(word))]

    if len(dists) == 1:
      if dists[0] <= 1:
        print(1)
        return 1

    for i in range(0, len(dists)-1):
      print(dists, i, i+1)
      if dists[i] <= 1 and dists[i+1] <= 1:
        res += 1
        dists[i] = 100
        dists[i+1] = 100

    for d in dists:
      if d <= 1:
        res += 1

    print(res)
    return res

s = Solution()
s.removeAlmostEqualCharacters(word = "aaaaa") # 2
s.removeAlmostEqualCharacters(word = "abddez") # 2
s.removeAlmostEqualCharacters(word = "zyxyxyz") # 3
s.removeAlmostEqualCharacters(word = "aa") # 1
s.removeAlmostEqualCharacters(word = "aac") # 1
s.removeAlmostEqualCharacters("aca") # 0
