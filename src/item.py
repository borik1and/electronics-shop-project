import csv


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
        # Item.all.append(self)
        # print(all)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Проверять, что длина наименования товара не больше
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

    @classmethod
    def instantiate_from_csv(cls, csv_file: str) -> list:
        # инициализируем экземпляры класса Item данными из файла src/items.csv
        items = []
        with open(csv_file, 'r', newline='', encoding='pt154') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
                Item.all.append(items)
        return items

    @staticmethod
    def string_to_number(value: str) -> int:
        try:
            # Преобразовать строку в число
            float_value = float(value)
            int_value = int(float_value)
            return int_value
        except ValueError:
            # Если преобразование не удалось, вернуть 0 или другое значение по умолчанию
            return 0
