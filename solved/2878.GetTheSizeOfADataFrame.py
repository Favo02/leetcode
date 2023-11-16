import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
  df = pd.DataFrame(players)
  r, c = df.shape
  return [r,c]
