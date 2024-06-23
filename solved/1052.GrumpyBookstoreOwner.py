class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cust = list(zip(customers, grumpy))
        happy = sum(c if g == 0 else 0 for c, g in cust)

        unhappy = list(
            map(lambda c: (c[0], c[1][0]),
            filter(lambda c: c[1][1] == 1,
            enumerate(cust))))

        start = time = gain = maxx = 0

        for end in range(len(unhappy)):
            time = (unhappy[end][0] - unhappy[start][0]) + 1
            gain += unhappy[end][1]

            while time > minutes:
                gain -= unhappy[start][1]
                start += 1
                time = (unhappy[end][0] - unhappy[start][0]) + 1

            maxx = max(maxx, gain)

        return happy + maxx
