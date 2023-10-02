class Solution():
  def winnerOfGame(self, colors):
    turn = True
    keep = True
    ai = 0
    bi = 0
    while keep:
      colTurn = 'A' if turn else 'B'
      startTurn = ai if turn else bi
      keep = False
      for c in range(startTurn+1, len(colors)-1):
        if colTurn == colors[c-1] == colors[c] == colors[c+1]:
          if turn:
            ai = c
          else:
            bi = c
          turn = not turn
          keep = True
          break
          
    print("res",not turn)
    return not turn
  
s = Solution()
s.winnerOfGame("AAABABB") # True
s.winnerOfGame("AA") # False
s.winnerOfGame("AAABBBAABBBAAA") # False
s.winnerOfGame("BBBAAAABB") # True
s.winnerOfGame("BBAAABBABBABB") # True
s.winnerOfGame("AAABABB") # True
s.winnerOfGame("AAAABBBB") # False
