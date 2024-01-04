class Solution:
  def numberOfBeams(self, bank: List[str]) -> int:
    rows = [s.count("1") for s in bank if "1" in s]
    res = sum(r1*r2 for r1, r2 in zip(rows, rows[1:]))
    print(res)
    return res
