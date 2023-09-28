from src.item import Item


class LanguageMixin:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

class Keyboard(Item):
    __language = "EN"

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def change_lang(self, lang: str):
        if lang == "EN" or lang == "RU":
            self.__language = lang
        raise ValueError("")
