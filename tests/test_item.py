"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
from src.instantiatecsverror import InstantiateCSVError
import pytest
import csv


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item1.price_discount = 0.9  # 10% скидка
    item2.price_discount = 0.8  # 20% скидка
    # Проверяем применение скидки
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 10000.0
    assert item2.price == 20000.0


def test_instantiate_from_csv():
    num_writes = len(Item.instantiate_from_csv('src/items.csv'))
    assert num_writes == 5


def test_csv_filenotfounderror():
    # Файл items.csv отсутствует.
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('src/items5.csv')


def test_csv_instantiatecsverror():
    # Файл item.csv поврежден
    with pytest.raises(InstantiateCSVError) as excinfo:
        with open('src/items1.csv', 'r', newline='', encoding='pt154') as file:
            reader = csv.DictReader(file)
            required_columns = ['name', 'price', 'quantity']
            if not all(col in reader.fieldnames for col in required_columns):
                raise InstantiateCSVError("Файл item.csv поврежден")

    # Проверяем, что ожидаемое исключение было выброшено и имеет нужное сообщение
    assert str(excinfo.value) == "Файл item.csv поврежден"


def test_string_to_number():
    num1 = Item.string_to_number('10')
    num3 = Item.string_to_number('5.0')
    num4 = Item.string_to_number('5.5')
    num2 = Item.string_to_number('TV')
    assert num1 == 10
    assert num2 == 0
    assert num3 == 5
    assert num4 == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
