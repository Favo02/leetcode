def solve(DIE_FACES, dice, target, mem, MOD):
  if (dice, target) in mem:
    return mem[(dice, target)]

  res = 0

  # no dice left to toss, 1 possible combination
  if dice == 0:
    # the target is always 0 due to the checks before the recursive call
    assert target == 0
    res = 1

  # one or more dice to tosses
  else:
    # try every face
    for face in range(1, DIE_FACES+1):
      # that is not too small to reach target with the tosses left
      if (dice-1)*DIE_FACES < target-face:
        continue
      # or not too big to reach target with the tosses left
      if dice-1 > target-face: # (dice-1)*1 as 1 is the smallest toss possible
        break
      res += solve(DIE_FACES, dice-1, target-face, mem, MOD)

  mem[(dice, target)] = res % MOD
  return res % MOD

class Solution:
  def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    res = solve(k, n, target, {}, 10**9 + 7)
    print(res)
    return res

s = Solution()
s.numRollsToTarget(1, 6, 3) # 1
s.numRollsToTarget(2, 6, 7) # 6
s.numRollsToTarget(3, 5, 12) # 10
s.numRollsToTarget(30, 30, 50) # 527148437
s.numRollsToTarget(30, 30, 500) # 222616187
