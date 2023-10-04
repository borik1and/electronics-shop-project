import csv

from src.instantiatecsverror import InstantiateCSVError


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

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        # сложение по количеству товара в магазине
        return None

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
    def instantiate_from_csv(cls, csv_file: str = 'items.csv') -> list:
        items = []
        try:
            with open(csv_file, 'r', newline='', encoding='pt154') as file:
                reader = csv.DictReader(file)

                # Проверка, что reader.fieldnames не равен None
                if reader.fieldnames is None:
                    raise InstantiateCSVError("Файл item.csv пуст")

                # Проверка заголовков столбцов в CSV файле
                required_columns = ['name', 'price', 'quantity']
                if not all(col in reader.fieldnames for col in required_columns):
                    print("Файл item.csv поврежден")

                for row in reader:
                    try:
                        name = row['name']
                        price = cls.string_to_number(row['price'])
                        quantity = int(row['quantity'])
                        item = cls(name, price, quantity)
                        items.append(item)
                        Item.all.append(item)
                    except ValueError as e:
                        print(f"Ошибка при чтении строки из CSV файла: {e}")
                    except KeyError as e:
                        print(f"Отсутствует ключ {e} в строке CSV файла.")

        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError:
            print(f"Ошибка при чтении CSV файла: {e}")

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
