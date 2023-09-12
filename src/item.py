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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """проверять, что длина наименования товара не больше
        10 симвовов. В противном случае, обрезать строку
        (оставить первые 10 символов)."""
        if len(value) > 10:
            value = value[:10]
        self.__name = value

    def calculate_total_price(self) -> float:
        return self.price * self.quantity
        # Рассчитывает общую стоимость конкретного товара в магазине.
        #  :return: Общая стоимость товара.
        pass

    def apply_discount(self) -> None:
        self.price *= self.pay_rate
        # Применяет установленную скидку для конкретного товара.
