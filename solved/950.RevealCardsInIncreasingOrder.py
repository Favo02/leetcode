class Solution:
  def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    deck.sort()

    sim = deque(range(len(deck)))
    res = []
    while sim:
      res.append(sim.popleft())
      if sim:
        sim.append(sim.popleft())

    arr = [0] * len(deck)
    for n, i in zip(deck, res):
      arr[i] = n
    return arr
