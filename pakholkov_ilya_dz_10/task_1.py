class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for el in self.matrix:
            print(*el)
        return f''

    def __add__(self, other):
        text = f'Невозможно сложить матрицы разного порядка\n'
        if len(self.matrix) != len(other.matrix):
            return text
        elif len(self.matrix[0]) != len(other.matrix[0]):
            return text
        else:
            new_matrix = []
            for i in range(0, len(self.matrix)):
                line = []
                for n in range(0, len(self.matrix[i])):
                    line.append(self.matrix[i][n] + other.matrix[i][n])
                new_matrix.append(line)
            [print(*el) for el in new_matrix]
            return f''


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
matrix_3 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_4 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_4)
