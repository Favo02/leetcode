class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"

        res = []
        if (abs(numerator) // numerator) * (abs(denominator) // denominator) == -1:
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        res.append(numerator // denominator)

        num = (numerator % denominator) * 10
        if num == 0:
            return "".join(map(str, res))

        res.append(".")

        dec = []
        seen = {}
        rep = None

        while num != 0:
            r, num = divmod(num, denominator)
            dec.append(r)

            num *= 10
            if num in seen:
                rep = seen[num]
                break

            seen[num] = len(dec)

        if rep is not None:
            dec = [*dec[:rep], "(", *dec[rep:], ")"]

        res += dec
        return "".join(map(str, res))
