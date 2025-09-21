class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}
        self.rows = rows

    def coords(self, cell):
        col, row = cell[0], int(cell[1:])
        assert 0 < row <= self.rows
        assert 'A' <= col <= 'Z'
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.coords(cell)
        self.cells[(row, col)] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.coords(cell)
        self.cells.pop((row, col), None)

    def getValue(self, formula: str) -> int:
        assert formula[0] == "="
        op1, op2 = formula[1:].split("+")
        op1 = int(op1) if op1.isdigit() else self.cells.get(self.coords(op1), 0)
        op2 = int(op2) if op2.isdigit() else self.cells.get(self.coords(op2), 0)
        return op1 + op2
