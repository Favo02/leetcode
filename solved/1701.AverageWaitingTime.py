class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        last = 0
        totwait = 0
        for arr, lenn in customers:
            end = max(last, arr) + lenn
            totwait += end - arr
            last = end

        return totwait / len(customers)
