from src.item import Item


class Phone(Item):
    """
    Дочерний класс от Item для представления телефонов в магазине
    """

    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса Phone
        param number_of_sim: количество SIM-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Переопределение метода __repr__
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Получение количества SIM-карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """
        Установление количества SIM-карт при выполнении условия (количество SIM-карт > 0)
        """
        if isinstance(number, int) and number > 0:
            self.__number_of_sim = number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
