class two_dimensions:
    def __init__(self,lowcol, upcol,lowrow, uprow):

        self.upcol = upcol
        self.uprow = uprow
        self.lowcol = lowcol
        self.lowrow = lowrow

        row = self.uprow - self.lowrow + 1
        col = self.upcol - self.lowcol + 1

        self.values = [[None for i in range(row)] for j in range(col)]

        self.values [0][0] = 9
        self.values[0][2] = 2
        self.values[6][4] = 64
        print(self.values)


    def getValue(self, col, row):
        return self.values[col - self.lowcol][row - self.lowrow]

my_arry = two_dimensions(1,10,2000,2010)
print(my_arry.getValue(1, 2000))
print(my_arry.getValue(7, 2004))






