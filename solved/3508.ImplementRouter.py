from typing import List
from collections import deque
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.destinations = {}
        self.dindex = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.seen:
            return False

        if destination not in self.destinations:
            self.destinations[destination] = []
            self.dindex[destination] = 0

        if len(self.queue) == self.limit:
            self.forwardPacket()

        self.queue.append((source, destination, timestamp))
        self.seen.add((source, destination, timestamp))
        self.destinations[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue: return []
        rem = self.queue.popleft()
        self.seen.remove(rem)
        s, d, t = rem
        assert self.destinations[d][self.dindex[d]] == t
        self.dindex[d] += 1
        return list(rem)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destinations: return 0
        s = max(bisect_left(self.destinations[destination], startTime), self.dindex[destination])
        e = max(bisect_right(self.destinations[destination], endTime), self.dindex[destination])
        return e - s
