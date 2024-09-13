# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = []
        for _ in range(m):
            matrix.append([-1] * n)

        x, y = 0, 0

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        d = 0

        while head:
            matrix[y][x] = head.val
            head = head.next

            cx, cy = dir[d % 4]
            if not (0 <= x+cx < n):
                d += 1
            elif not (0 <= y+cy < m):
                d += 1
            elif matrix[y+cy][x+cx] != -1:
                d += 1

            cx, cy = dir[d % 4]
            x, y = x+cx, y+cy

        return matrix
