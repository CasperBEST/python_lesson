class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Wage': wage, 'Bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'

    def get_total_income(self):
        total_income = sum(self._income.values())
        return f'Wages including bonus: {total_income}'


# создаем объекты класса Position
worker_1 = Position('Ridley', 'Scott', 'Director', 100000, 30000)
worker_2 = Position('Matt', 'Damon', 'Programmer', 80000, 25000)
worker_3 = Position('Jessica', 'Chastain', 'Chief accountant', 60000, 20000)

# Проверяем атрибуты (наследуемые из класса Worker) и методы класса Position
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1._income)  # защищенный атрибут
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_2.name)
print(worker_2.surname)
print(worker_2.position)
print(worker_2._income)  # защищенный атрибут
print(worker_2.get_full_name())
print(worker_2.get_total_income())
print(worker_3.name)
print(worker_3.surname)
print(worker_3.position)
print(worker_3._income)  # защищенный атрибут
print(worker_3.get_full_name())
print(worker_3.get_total_income())
