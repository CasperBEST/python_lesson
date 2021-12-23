class MyValiDate(Exception):
    pass


class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def get_int(cls, text):
        data_list_int = []
        for i in text.split('-'):
            data_list_int.append(int(i))
        return data_list_int

    @staticmethod
    def validate_date(self):
        data_int = Date.get_int(self)
        if 0 < data_int[0] < 31:
            pass
        else:
            raise MyValiDate(f"Не существует дня {data_int[0]}. Число должно быть в диапазоне от 1 до 31.")
        if 0 < data_int[1] < 12:
            pass
        else:
            raise MyValiDate(f"Не существует месяца номер {data_int[1]}. Число должно быть в диапазоне от 1 до 12")
        if data_int[2] < 1:
            raise MyValiDate(f"Год не может быть меньше 1")


data_1 = Date('19-02-1981')

print(data_1.date, type(data_1.date))

for el in Date.get_int('19-02-1981'):
    print(type(el))

Date.validate_date('32-02-1981')  # Выдаст ошибку
