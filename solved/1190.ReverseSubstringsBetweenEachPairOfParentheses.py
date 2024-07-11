class Solution:
    def reverseParentheses(self, s: str) -> str:
        def scan(buffer):
            cur = deque()

            while buffer:
                b = buffer.popleft()
                if b == ")":
                    break
                elif b == "(":
                    cur += reversed(scan(buffer))
                else:
                    cur.append(b)

            return cur

        res = scan(deque(s))
        return "".join(res)
