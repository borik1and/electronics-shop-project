from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
