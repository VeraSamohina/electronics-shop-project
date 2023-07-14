import csv
import os.path


class InstantiateCSVError(Exception):
    """
    Класс для исключения при инициализации CSV-файла
    """
    def __init__(self, *args) -> None:
        self.message = args[0] if args else None


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
        self.all.append(self)

    def __repr__(self):
        """
        Вывод информации о товаре.
        :return: Строка с информацией о товаре.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Преобразование экземпляра класса item в строку.
        """
        return self.__name

    def __add__(self, other):
        """
        Сложение двух экземпляров класса Item(и дочерних).
        :param other: Экземпляр класса Item.
        :return: Количество двух экземпляров класса Item.
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Item и дочерние от них.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Длина наименования товара превышает 10 символов')
            self.__name = name[:10]

    @staticmethod
    def string_to_number(value):
        """
        Преобразование строки в целое число.
        :param value: Строка.
        :return: целое число.
        """
        value = int(float(value))
        return value

    @classmethod
    def instantiate_from_csv(cls, path_file_name):
        """
        Создание экземпляров класса Item из файла.
        """
        Item.all.clear()
        if os.path.exists(path_file_name):
            csvfile = open(path_file_name, newline='')
            reader = csv.DictReader(csvfile, fieldnames=None, dialect='excel')
        else:
            raise FileNotFoundError('Отсутствует файл items.csv')
        if len(reader.fieldnames) != 3:
            raise InstantiateCSVError('Файл items.csv поврежден')
        else:
            for row in reader:
                Item(row['name'], Item.string_to_number(row['price']), Item.string_to_number(row['quantity']))
            csvfile.close()

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
