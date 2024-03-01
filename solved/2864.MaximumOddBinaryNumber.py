class Solution:
  def maximumOddBinaryNumber(self, s: str) -> str:
    return "".join(["1" if i < s.count("1")-1 else "0" for i in range(len(s)-1)] + ["1"])
