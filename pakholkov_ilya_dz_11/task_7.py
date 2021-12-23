class ComplexNumber:
    def __init__(self, number):
        self.number = complex(number)

    def __add__(self, other):
        return ComplexNumber(self.number + other.number)

    def __mul__(self, other):
        return ComplexNumber(self.number * other.number)

    def __str__(self):
        return f"{self.number}"


a = ComplexNumber(1 + 2j)
b = ComplexNumber(2 + 3j)

print(a + b)
print(a * b)
