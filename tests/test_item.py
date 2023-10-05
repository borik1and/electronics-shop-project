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


def test_csv_file_not_found_error():
    with pytest.raises(FileNotFoundError) as excinfo:
        with open('src/items30.csv', 'r', newline='', encoding='pt154') as file:
            reader = csv.DictReader(file)
    # Проверяем, что ожидаемое исключение было выброшено и имеет нужное сообщение
    assert str(excinfo.value) == "[Errno 2] No such file or directory: 'src/items30.csv'"


def test_instantiate_csv_error_message():
    with pytest.raises(InstantiateCSVError) as exc_info:
        # Вызываем вашу функцию, которая может вызвать InstantiateCSVError
        Item.instantiate_from_csv('src/items1.csv')

    # Проверяем, что исключение было вызвано
    assert exc_info.type == InstantiateCSVError

    # Проверяем сообщение исключения
    assert str(exc_info.value) == 'Файл item.csv поврежден'



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
