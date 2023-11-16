import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
  heavy = animals[animals["weight"] > 100]
  sorted = heavy.sort_values(by="weight", ascending=False)
  return sorted[["name"]]
