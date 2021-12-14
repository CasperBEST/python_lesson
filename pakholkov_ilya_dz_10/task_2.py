from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.expence

    def __str__(self):
        return f'Coat: size {self.size}, fabric consumption {self.expence},' \
               f'total fabric consumption {Coat.expence_count:.02f}'

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Costume.expence_count += self.expence

    def __str__(self):
        return f'Costume: size {self.height}, fabric consumption {self.expence},' \
               f'total fabric consumption {Coat.expence_count:.02f}'

    @property
    def expence(self):
        exp = (self.height * 2 + 0.3) / 100
        return float(f'{exp:.02f}')


cloth_1 = Coat(48)
print(cloth_1)
cloth_2 = Coat(52)
print(cloth_2)
cloth_3 = Costume(170)
print(cloth_3)
cloth_4 = Costume(180)
print(cloth_4)
