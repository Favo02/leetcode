class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        rank = {val:i+1 for i, val in enumerate(sorted(list(set(arr))))}
        return [rank[a] for a in arr]
