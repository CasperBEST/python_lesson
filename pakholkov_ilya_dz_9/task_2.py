class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        result = self._length * self._width * 25 * 0.01 / 1000
        print(f'Масса асфальта, для покрытия дороги, '
              f'длиной {self._length/1000} км. и шириной {self._width} м. '
              f'равняется {result} тонн.')


road = Road(50000, 25)
road.calc_mass()
