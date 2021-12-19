class Warehouse:
    def __init__(self):
        self.products = []

    def entry(self, product):
        self.products.append(product)

    def transfer(self, product):
        if product in self.products:
            self.products.remove(product)

    @property
    def count(self):
        return f"Количество техники на складе: {len(self.products)}"


class OfficeEquipment:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__} {self.model}, with price {self.price}"


class Printer(OfficeEquipment):
    def __init__(self, model, price, a_type):
        super().__init__(model, price)
        self.a_type = a_type


class Scanner(OfficeEquipment):
    def __init__(self, model, price, size):
        super().__init__(model, price)
        self.size = size


class Ifi(OfficeEquipment):
    def __init__(self, model, price, speed):
        super().__init__(model, price)
        self.speed = speed


product_1 = Printer('HP', 10000, 'laser')
product_2 = Printer('Samsung', 8000, 'Jet')
product_3 = Scanner('Canon', 12000, 'A3')
product_4 = Scanner('Epson', 15000, 'A5')
product_5 = Ifi('Canon', 11000, 20)
product_6 = Ifi('Brother', 15000, 30)

print(product_4)

hub_1 = Warehouse()
hub_1.entry(product_1)
hub_1.entry(product_2)
hub_1.entry(product_3)
hub_1.entry(product_4)
hub_1.entry(product_5)
hub_1.entry(product_6)

print(hub_1.count)
