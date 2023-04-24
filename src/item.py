from csv import DictReader


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'поврежден'

    def __str__(self):
        return f'{self.message}'


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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

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
        try:
            with open(file, 'r', newline='', encoding='windows-1251') as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    if len(row) < 3 or row.get(None):
                        raise InstantiateCSVError
                    cls(row['name'], float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            print(f'Отсутствует файл {file}')
            return f'Отсутствует файл {file}'
        except InstantiateCSVError as e:
            print(f'{file} {e}')
            return f'{file} {e}'





