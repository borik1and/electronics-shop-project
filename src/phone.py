from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, num_sim_card):
        super().__init__(name, price, quantity)
        self.num_sim_card = num_sim_card


