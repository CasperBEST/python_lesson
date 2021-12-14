class Cell:
    def __init__(self, cell_cells):
        self.cell_cells = int(cell_cells)

    def __str__(self):
        return f'{self.__class__.__name__} with {self.cell_cells} cells'

    def __add__(self, other):
        return Cell(self.cell_cells + other.cell_cells)

    def __sub__(self, other):
        if self.cell_cells - other.cell_cells <= 0:
            raise ValueError("Невозможно произвести вычитание! Разность должна быть больше нуля!")
        return Cell(self.cell_cells - other.cell_cells)

    def __mul__(self, other):
        return Cell(self.cell_cells * other.cell_cells)

    def __floordiv__(self, other):
        if self.cell_cells // other.cell_cells == 0:
            raise ValueError("Значение первой клетки должно быть больше чем значение второй!")
        return Cell(self.cell_cells // other.cell_cells)

    def make_order(self, line):
        return print(('*' * line + '\n') * (self.cell_cells // line) + ('*' * (self.cell_cells % line)))


cell_1 = Cell(40)
cell_2 = Cell(2)
print(cell_1)
print(cell_2)
cell_3 = cell_1 + cell_2
print(cell_3)
# cell_4 = cell_2 - cell_1
# print(cell_4)
cell_4 = cell_1 - cell_2
print(cell_4)
cell_5 = cell_1 * cell_3
print(cell_5)
cell_6 = cell_5 // cell_1
print(cell_6)
cell_1.make_order(7)
