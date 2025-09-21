from typing import List
from heapq import heappop, heappush
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(list) # movie -> sorted[(price, shop)]
        self.available = {} # dict(shop, movie) -> rented
        self.prices = {} # dict(shop, movie) -> price

        self.rented = [] # heap[(price, shop, movie)]
        self.inrented = set() # set{(price, shop, movie)}

        for s, m, p in entries:
            self.movies[m].append((p, s))
            self.available[(s, m)] = True
            self.prices[(s, m)] = p

        for m, ps in self.movies.items():
            self.movies[m] = sorted(ps)

    def search(self, movie: int) -> List[int]:
        res = []
        for p, s in self.movies[movie]:
            if self.available[(s, movie)]:
                res.append(s)
            if len(res) == 5: break
        return res

    def rent(self, shop: int, movie: int) -> None:
        assert (shop, movie) in self.available
        assert self.available[(shop, movie)]
        self.available[(shop, movie)] = False
        if (self.prices[(shop, movie)], shop, movie) not in self.inrented:
            heappush(self.rented, (self.prices[(shop, movie)], shop, movie))
            self.inrented.add((self.prices[(shop, movie)], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        assert (shop, movie) in self.available
        assert self.available[(shop, movie)] is False
        self.available[(shop, movie)] = True

    def report(self) -> List[List[int]]:
        res = []
        while self.rented:
            p, s, m = heappop(self.rented)
            if self.available[(s, m)]:
                self.inrented.remove((p, s, m))
                continue
            res.append((p, s, m))
            if len(res) == 5: break
        for e in res:
            heappush(self.rented, e)
        return [[s, m] for p, s, m in res]
