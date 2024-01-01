from typing import List
from bisect import insort

class FoodRatings:

  def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    self.food_to_cuisine = {} # food to cuisine
    self.food_to_rating = {} # food to rating
    self.cuisines = {} # cuisine to foods (sorted)

    for f, c, r in zip(foods, cuisines, ratings):
      self.food_to_cuisine[f] = c
      self.food_to_rating[f] = r

      if c not in self.cuisines:
        self.cuisines[c] = []
      insort(self.cuisines[c], (-r, f)) # inverse rating for decreasing order

  def changeRating(self, food: str, newRating: int) -> None:
    c = self.food_to_cuisine[food]
    self.food_to_rating[food] = newRating
    # insert another rating, without removing old one
    insort(self.cuisines[c], (-newRating, food))

  def highestRated(self, cuisine: str) -> str:
    for r,f in self.cuisines[cuisine]:
      # check if the rating is valid (updated)
      if -r == self.food_to_rating[f]:
        return f
