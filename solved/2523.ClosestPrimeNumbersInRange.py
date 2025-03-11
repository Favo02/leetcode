def sieve(n):
  prime = [True for _ in range(n+1)]
  p = 2
  while (p * p <= n):
    if (prime[p] == True):
      for i in range(p * p, n+1, p):
        prime[i] = False
    p += 1
  for p in range(2, n+1):
    if prime[p]:
      yield p

class Solution:
  def closestPrimes(self, left: int, right: int) -> List[int]:
    primes = [p for p in sieve(right) if p >= left]

    if len(primes) < 2:
      return [-1, -1]

    min = float("inf")

    for a, b in zip(primes, primes[1:]):
      if b-a < min:
        min = b-a
        res = [a, b]

    return res
