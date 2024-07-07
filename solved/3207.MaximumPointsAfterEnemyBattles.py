from typing import List
import math

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:

        points = 0

        enemyEnergies.sort(reverse=True)
        used = 0

        tofarm = enemyEnergies[-1]

        while used < len(enemyEnergies):

            if currentEnergy >= tofarm:
                points += math.floor(currentEnergy / tofarm)
                currentEnergy = currentEnergy % tofarm
            elif points >= 1:
                currentEnergy += enemyEnergies[used]
                used += 1
            else:
                break

        print(points)
        return points

s = Solution()
s.maximumPoints([3,2,2], 2)
s.maximumPoints([2], currentEnergy = 10)
