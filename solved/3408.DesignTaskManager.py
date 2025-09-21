from typing import List
from heapq import heappop, heappush

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.priorities = {}
        self.users = {}
        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.priorities[taskId] = priority
        self.users[taskId] = userId
        heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.priorities[taskId] = newPriority
        heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.priorities[taskId]
        del self.users[taskId]

    def execTop(self) -> int:
        while self.heap:
            pr, id = map(lambda n: -n, heappop(self.heap))
            if id not in self.priorities: continue
            if pr != self.priorities[id]: continue
            res = self.users[id]
            self.rmv(id)
            return res
        return -1
