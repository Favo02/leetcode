class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for i, (arr, leave) in enumerate(times):
            events.append((arr, True, i))
            events.append((leave, False, i))
        events.sort()

        friends = [-1] * len(times)

        empty = []
        count = 0

        for _, arr, friend in events:
            seat = None
            if arr:
                if empty:
                    seat = heapq.heappop(empty)
                else:
                    seat = count
                    count += 1

                if friend == targetFriend:
                    return seat

                friends[friend] = seat

            else:
                heapq.heappush(empty, friends[friend])

        assert False
