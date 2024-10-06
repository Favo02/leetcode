class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        val = skill[0] + skill[-1]
        res = 0

        for i in range(len(skill)//2):
            if skill[i] + skill[-i-1] != val:
                return -1
            res += skill[i] * skill[-i-1]

        return res
