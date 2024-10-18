class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a == b == c == 0:
            return ""

        order = sorted([[a, 'a'], [b, 'b'], [c, 'c']], reverse=True)

        res = []
        last = ''
        while (len(order) > 0) and not (len(order) == 1 and last == order[0][1]):

            # take biggest
            if order[0][1] != last:

                if order[0][0] >= 2:
                    order[0][0] -= 2
                    res.append(order[0][1])
                    res.append(order[0][1])

                else:
                    order[0][0] -= 1
                    res.append(order[0][1])

                last = order[0][1]

            # take second biggest
            else:
                order[1][0] -= 1
                res.append(order[1][1])
                last = order[1][1]

            order = sorted(filter(lambda x: x[0] > 0, order), reverse=True)

        return "".join(res)
