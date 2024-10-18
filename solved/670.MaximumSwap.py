class Solution:
    def maximumSwap(self, num: int) -> int:
        snum = str(num)
        places = [snum.rfind(str(i)) for i in range(10)]

        res = list(snum)
        for index, curdigit in enumerate(snum):
            for j in range(9, -1, -1):
                if int(curdigit) < j and places[j] > index:
                    res[index], res[places[j]] = res[places[j]], res[index]
                    return int("".join(res))

        return num
