class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(a%2==1 and b%2==1 and c%2==1 for a, b, c in zip(arr, arr[1:], arr[2:]))
