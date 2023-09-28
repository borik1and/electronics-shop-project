from src.phone import Phone


def test_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1 + phone1 == 10


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    try:
        phone1.number_of_sim = 0
        # Если никаких исключений не делается, то испытание не проходит
        assert False, "Ожидается ValueError"
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."
