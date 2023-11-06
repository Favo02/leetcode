class SeatManager:

  def __init__(self, n: int):
    self.free = n
    self.next = 1
    self.jumps = []

  def reserve(self) -> int:
    res = None
    self.free -= 1

    if self.jumps:
      self.jumps.sort()
      res = self.jumps[0]
      self.jumps = self.jumps[1:]
    else:
      res = self.next
      self.next += 1

    return res

  def unreserve(self, seatNumber: int) -> None:
    self.free += 1
    self.jumps.append(seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
