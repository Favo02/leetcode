class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for l in logs:
            if l == "./":
                continue
            elif l == "../":
                level = max(0, level-1)
            else:
                level += 1
        return level
