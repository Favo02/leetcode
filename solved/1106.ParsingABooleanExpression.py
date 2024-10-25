class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == "t":
            return True

        if expression == "f":
            return False

        if expression[0] == "!":
            return not self.parseBoolExpr(expression[2:-1])

        if expression[0] == "&":
            bal = 0
            start = 2
            res = True
            for end in range(2, len(expression)-1):
                if expression[end] == "(": bal += 1
                elif expression[end] == ")": bal -= 1
                elif bal == 0 and expression[end] == ",":
                    res &= self.parseBoolExpr(expression[start:end])
                    start = end+1
                if not res: return False
            res &= self.parseBoolExpr(expression[start:-1])
            return res

        if expression[0] == "|":
            bal = 0
            start = 2
            res = False
            for end in range(2, len(expression)-1):
                if expression[end] == "(": bal += 1
                elif expression[end] == ")": bal -= 1
                elif bal == 0 and expression[end] == ",":
                    res |= self.parseBoolExpr(expression[start:end])
                    start = end+1
                if res: return True
            res |= self.parseBoolExpr(expression[start:-1])
            return res

        assert False
