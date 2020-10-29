from random import randint, choice

class Sudoku:
    def __init__(self):
        self.grid = [[(col * 3 + col // 3 + row) % 9 + 1 for row in range(9)] for col in range(9)]

    def show(self):
        print(*self.grid, sep = "\n")

    def transp(self):
        self.grid = list(map(list, zip(*self.grid)))

    def swap_rows_small(self):
        squareRow = choice([0, 3, 6]);
        rows = [0, 1, 2]; rows.pop(randint(1, 3) - 1)
        rowFirst, rowSecond = rows
        self.grid[squareRow + rowFirst], self.grid[squareRow + rowSecond] = self.grid[squareRow + rowSecond], self.grid[squareRow + rowFirst]

    def swap_rows_big(self):
        squareRow = [0, 3, 6]; squareRow.pop(randint(1, 3) - 1)
        squareRowFirst, squareRowSecond = squareRow
        self.grid[squareRowFirst:squareRowFirst + 3], self.grid[squareRowSecond:squareRowSecond + 3] = self.grid[squareRowSecond:squareRowSecond + 3], self.grid[squareRowFirst:squareRowFirst + 3]

    def swap_cols_small(self):
        Sudoku.transp(self)
        Sudoku.swap_rows_small(self)
        Sudoku.transp(self)    

    def swap_cols_big(self):
        Sudoku.transp(self)
        Sudoku.swap_rows_big(self)
        Sudoku.transp(self)

    def shuffle(self, iterCount = 100):
        shuffleFunc = ["self.swap_rows_small()", "self.swap_rows_big()", "self.swap_cols_small()", "self.swap_cols_big()"]
        for i in range(iterCount):
            eval(choice(shuffleFunc))

            
        
a = Sudoku()
a.shuffle()
a.show()