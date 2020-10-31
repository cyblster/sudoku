from random import randint, choice

class Sudoku:
    def __init__(self):
        self.grid = [[(col * 3 + col // 3 + row) % 9 + 1 for row in range(9)] for col in range(9)]

    def show(self):
        for row in self.grid:
            print(*row)

    def transp(self):
        self.grid = list(map(list, zip(*self.grid)))

    def swapRowsSmall(self):
        squareRow = choice([0, 3, 6]);
        rows = [0, 1, 2]; rows.pop(randint(1, 3) - 1)
        rowFirst, rowSecond = rows
        self.grid[squareRow + rowFirst], self.grid[squareRow + rowSecond] = self.grid[squareRow + rowSecond], self.grid[squareRow + rowFirst]

    def swapRowsBig(self):
        squareRow = [0, 3, 6]; squareRow.pop(randint(1, 3) - 1)
        squareRowFirst, squareRowSecond = squareRow
        self.grid[squareRowFirst:squareRowFirst + 3], self.grid[squareRowSecond:squareRowSecond + 3] = self.grid[squareRowSecond:squareRowSecond + 3], self.grid[squareRowFirst:squareRowFirst + 3]

    def swapColsSmall(self):
        Sudoku.transp(self)
        Sudoku.swapRowsSmall(self)
        Sudoku.transp(self)    

    def swapColsBig(self):
        Sudoku.transp(self)
        Sudoku.swapRowsBig(self)
        Sudoku.transp(self)

    def shuffle(self, iterCount = 10000):
        shuffleFunc = ["self.swapRowsSmall()", "self.swapRowsBig()", "self.swapColsSmall()", "self.swapColsBig()"]
        for _ in range(iterCount):
            eval(choice(shuffleFunc))
        
a = Sudoku()
a.shuffle()
a.show()