class Solution:
  def longestIdealString(self, s: str, k: int) -> int:

    def charToIndex(c):
      return ord(c) - ord('a')

    best = [0] * 26

    for i in range(len(s)):

      char = charToIndex(s[i])
      best[char] = 1 + max(best[max(0, char-k): min(26, char+k+1)])

    print(max(best))
    return max(best)

s = Solution()
s.longestIdealString("acfgbd", k = 2) # 4
s.longestIdealString(s = "abcd", k = 3) # 4
s.longestIdealString("pvjcci", 4) # 2
s.longestIdealString("dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb", 7)
