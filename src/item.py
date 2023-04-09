import csv
from typing import List, Any


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    @staticmethod
    def string_to_number(string: str):
        """
        преобразует строку в число
        """
        return int(float(string))

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина не может превышать 10 символов')
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        """
        Заполняет список товаров из файла csv
        """
        Item.all.clear()
        with open(file, 'r', newline='', encoding='windows-1251') as csvfile:
            result = csv.reader(csvfile)
            header = next(result)
            for row in result:
                name, price, quantity = row
                cls(name, price, quantity)



