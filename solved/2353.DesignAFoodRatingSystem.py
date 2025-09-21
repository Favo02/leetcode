from typing import List
from heapq import heappop, heappush

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {f: r for f, r in zip(foods, ratings)}
        self.cuisine = {f: c for f, c in zip(foods, cuisines)}
        self.rankings = {c: [] for c in cuisines}
        for f, c, r in zip(foods, cuisines, ratings):
            heappush(self.rankings[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating
        heappush(self.rankings[self.cuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.rankings[cuisine]:
            r, f = self.rankings[cuisine][0]
            if self.ratings[f] == -r:
                return f
            heappop(self.rankings[cuisine])
